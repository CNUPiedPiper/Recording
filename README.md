# To satisfy dependency:

## Linux
#### You may use sudoer.

	$apt-get install python-dev
	
	$cd GoogleCloudPlatform/speech/cloud-client
	$pip install -r requirement.txt

#### if you failed on this section, after complete what pip saying, *try pip install --upgrade -r requirement.txt* again.

	$apt-get install python-pyaudio
	
	$cd ../../../sample

#### With get_dev_index.py, modify device number in recoding.py code to number that mic has.

	$export export GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>

# To use:

	$cd sample
	$python2 recording.py

#### After this, sound.raw file is made.

	$cd ../GoogleCloudPlatform/speech/cloud-client
	$python2 transcribe_streaming.py path/to/sound.raw
