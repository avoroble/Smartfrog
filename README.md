# Smartfrog test assignment
## Theoretical part
### Tasks definition
You are in charge of product quality control for a brand new action camera. The camera is rated to be water resistant for up to 100m, up to 15m vertical fall and guaranteed battery life of 10 hours standby time or 4 hours filming time. The camera has a power button, shutter button and mode switch button, which toggles between video and still image capture. Please write a test plan with at least 15 items, each consisting of a test description, test procedure steps and the expected results for each step (pass/fail criteria).

### Test Plan for Action Camera
#### 1. Test Scope
##### In-Scope
Verification of the camera’s core functions such as power on/off, shutter button, and mode switch.
Testing of water resistance, fall resistance, and overall durability.
Battery performance in standby and filming modes.
Charging functionality.
##### Out-of-Scope
Data storage (internal, external).
Audio, video, and image capture quality incl. custom settings (e.g., filters, resolution).
Third-party accessories compatibility.
Firmware testing or updates post-production.
#### 2. Context of Testing
##### Testing Objectives
Ensure the camera meets its functional specifications, performance standards, and durability requirements.
Validate the camera’s ability to withstand typical user conditions (water exposure, drops, battery usage).
##### Testing Environment
- standard operating conditions (indoor, room temperature, outdoor, etc.).
- pressurized water tank to mimic high-pressure environment.
##### Testing Equipment
- Action camera
- Charging station
- Computer for data transfer
##### Testing Tools
- Stopwatch
- Water tank (for immersion testing)
- Height measurement tool (for drop test)
- Data transfer software.

##### Assumptions and Constraints
###### Assumptions
- The following terms are used in the test plan as abstractions since they are not explicitly mentioned in the product specification, but are assumed to be present: 'battery charge indicator', 'power indicator', 'camera charge indicator', 'video recording mode indicator', 'video recording indicator', 'image capture mode indicator'.
- Required testing equipment (e.g., water tank, drop surfaces) is available and functional.
- Testing will be conducted in controlled environments to simulate real-world use cases.

###### Constraints
- Availability of testing resources, such as qualified personnel or specific test tools.
- Environmental conditions such as extreme underwater pressure may not always be fully replicated in a controlled environment.

#### 3. Test documentation
#### Camera basic testing procedure
<img width="957" alt="image" src="https://github.com/user-attachments/assets/8cf31a92-0e02-4d1d-ab1e-66973d9d5657">

#### Test case documentation
<img width="957" alt="image" src="https://github.com/user-attachments/assets/92bff4cf-0e51-45e7-9788-064745754946">
<img width="957" alt="image" src="https://github.com/user-attachments/assets/34f3fe61-8993-438e-81cb-542ceaa5fce1">
<img width="957" alt="image" src="https://github.com/user-attachments/assets/9522b281-a574-4fd6-aecd-b1c830be942d">
<img width="957" alt="image" src="https://github.com/user-attachments/assets/3e7dce5c-6124-44e3-ad13-8ea6f82c142c">
<img width="957" alt="image" src="https://github.com/user-attachments/assets/e37a4dc1-9e1e-43f0-89a8-50f6ebfb5afd">
<img width="957" alt="image" src="https://github.com/user-attachments/assets/6c70333b-0e32-4776-82bc-3f69d309117e">
<img width="957" alt="image" src="https://github.com/user-attachments/assets/a7e3dd3b-97ec-41d4-b87e-d8c39d4b5ff3">

## Practical part
### Alphanumeric sort
#### Tasks definition
Write an implementation of an alphanumeric sort. In this case, we should sort numbers first, followed by lowercase letters, uppercase letters and then all other characters. The special case here is that if any two numerical characters are next to each other, then they will be treated as one numeric value. The following example has a sample input with the expected output.
Example:
Input -> ‘A11a4’
Output -> ‘411aA’
#### Deliverables
script: `alphanumeric_sort.py`
#### How to run
##### Pre-conditions for execution
1. Python should be installed on your local computer
2. The `alphanumeric_sort.py` file should be downloaded to your local computer.
##### Running the script
Execute the following command in the terminal window: `python alphanumeric_sort.py`.
##### Input data
After the script is executed in the terminal window, it will request the input string that is meant to be sorted.
##### Execution results
The sorted string will appear in the terminal window.

### Archiver
#### Tasks definition
Write a script that can be run in the background that does the following:
- On startup make sure there is a “tmp” sub folder in the current directory.
- If one does not exist, it creates it.
- Repeatedly counts the number of files in the “tmp” folder.
- Whenever the number of files reaches 10, the script creates an archive “files.tar.gz” with all 10 files from the “tmp” directory.
- The script should then empty the folder and print “files collected” to the console before.
exiting.
#### Deliverables
script: `archive_files.py` - archives the files in the `tmp/` folder.<br>
script: `create_files.py` - creates 10 files in the `tmp/` folder.
#### How to run
##### Pre-conditions for execution
1. Python should be installed on the local computer.
2. `archive_files.py`, `create_files.py` files should be downloaded to the working directory.
##### How to run
1. Open the first terminal window and execute the following command: `archive_files.py`.
2. The script will run in the background, waiting for 10 files to appear in the `tmp/` folder.
3. Open the seccond terminal window and execute the following command: `create_files.py`.
##### Execution results
The archive file `files.tar.gz` should be stored in working directory.













