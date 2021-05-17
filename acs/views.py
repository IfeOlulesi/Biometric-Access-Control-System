from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Student, Tracker
from os.path import isfile, join
from PIL import Image
from os import listdir

import random, pytz, base64, imagehash

def base64_to_jpeg(pic):
  """
  Accepts a picture in base64 string, 
  encodes that string,
  converts it to a .jpeg image 
  and saves it on the file system
  """

  # converts the base 64 string to bytes and decodes those bytes
  image_64_decode = base64.decodebytes(pic.encode())   
  # create a writable image 
  image_result = open('media/buffer/fprint_check.jpeg', 'wb') 
  # and write the decoding result
  image_result.write(image_64_decode)
  

def check_similarity(img1_rel_path, img2_rel_path):
  """
  Arguments: 
  img1_rel_path -- the relative path to the location of the first image
  img2_rel_path -- the relative path to the location of the second image

  Accepts two images, compares them,
  and returns the difference between them -> int
  
  """

  hash0 = imagehash.average_hash(Image.open(img1_rel_path)) 
  hash1 = imagehash.average_hash(Image.open(img2_rel_path)) 

  return hash0 - hash1


# Create your views here.
def index(request):
  return render(request, 'acs/index.html')
 

def auth(request):
  """
    STEP 1: Get the file names of all the fingerprints located on my file system
    STEP 2: Convert the incoming base64 into a .jpeg format and store on file system
    STEP 3: Compare the incoming fprint with all the other fprints ...
    STEP 4: and find the one with the highest match score
    STEP 5: Identify who owns that fingerprint
    
    STEP 6: Check if the student has signed in before

  """
  UNKNOWN_FPRINT_FPATH = "media/buffer/fprint_check.jpeg"

  # creates an aware datetime object at now
  d = datetime.now()
  timezone = pytz.timezone("Africa/Lagos")
  D_AWARE = timezone.localize(d) # aware datetime at NOW

  CUTOFF = 5

  # STEP 1 - orders them according to name ...probably 0 -> 9 ....
  known_fprints = [f for f in listdir('media/finger-print') if isfile(join('media/finger-print', f))]
  
  # STEP 2
  base64_fprint = request.POST['img-base64'] # incoming image to be matched in base64 format
  base64_to_jpeg(base64_fprint)

  # STEP 3
  list_of_difs = [] # the results here map respectively to the fprints in known_fprints
  
  for fprint in known_fprints:
    known_fprint_fpath = f"media/finger-print/{fprint} "
    list_of_difs.append(check_similarity(UNKNOWN_FPRINT_FPATH, known_fprint_fpath)) #
  # print(f"\nList of differences: {list_of_difs}")

  # STEP 4 - first render
  if min(list_of_difs) > CUTOFF: # if the fingerprint doesn't match any on the database
    return render(request, 'acs/result.html', {
      'status': 'Error 404: Student not found',
    })
    
  else: # if the fingerprint finds a match on the database
    closest_match_index = list_of_difs.index(min(list_of_difs)) # find the index of that match
    matched_known_fprint = known_fprints[closest_match_index] # find its map in known_fprints
    # print("\n Matched known fingerprint: "+matched_known_fprint+"\n")

    # STEP 5
    get_me = matched_known_fprint[:7]
    student_found = Student.objects.get(fingerprint__contains=get_me)

    ##### DEBUGGING STARTS
    # print(f"\nStudent found: {student_found} \n")

    # STEP 6
    # check if the latest tracker for that student has a sign out field that's filled
    list_of_trackers = student_found.tracker_set.order_by('-pk')
    # print(f'List of trackers: {list_of_trackers} \n')
    
    if list_of_trackers[0].time_out: # SIGN IN
      new_tracker = Tracker(student=student_found, time_in=D_AWARE)
      new_tracker.save()
      # print(f'Time in: {new_tracker.time_in}')

      return render(request, 'acs/result.html', {
      'student':student_found, 
      'time_in': new_tracker.time_in,
    })

      
    else: # SIGN OUT
      old_tracker = list_of_trackers[0]
      old_tracker.time_out = D_AWARE
      old_tracker.save()
      # print(f'Time out: {old_tracker.time_out}')

      return render(request, 'acs/result.html', {
      'student': student_found,
      'time_in': old_tracker.time_in,
      'time_out': old_tracker.time_out,
    })
    

def develop(request): 
  return render(request, 'acs/develop.html', {
    'student': 'Fred Hamilton',
    'time_in': '',
    'time_out': '',
  })
