import os
import re
from pathlib import Path

def extractDirId(dirName):
  pattern = re.compile(r'^question-(?P<id>\d+)')
  match = pattern.match(dirName)
  if (match == None):
    return 0

  return match.group('id')

def getNextId(dirName):
  dirList = filter(lambda dirPath: os.path.isdir(dirPath), os.listdir(dirName))
  dirIds = map(lambda dirName: extractDirId(dirName), dirList)
  dirIdNumbers = map(lambda dirIdString: int(dirIdString), dirIds)
  maxId = max(dirIdNumbers)
  nextId = maxId + 1
  return nextId

def createNewQuestion(dirName, nextId):
  newDirName = 'question-{:04d}'.format(nextId)
  print('next directory will be \'{}\''.format(newDirName))

  Path(f'{dirName}{newDirName}').mkdir()
  Path(f'{dirName}{newDirName}/question.md').touch()
  Path(f'{dirName}{newDirName}/answer.md').touch()
  Path(f'{dirName}{newDirName}/tags.txt').touch()

nextId = getNextId('./')
createNewQuestion('./', nextId)