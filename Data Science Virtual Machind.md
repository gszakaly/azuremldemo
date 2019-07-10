## Create Data Science Virtual Machine

Open https://portal.azure.com in a browser.

Open *All services*.

Under *AI + machine learning* select *Cognitive Services*.

Select *Add*.

Select *Data Science Virtual Machine for Linux (Ubuntu)* and click *Create*.

Under *Resource group* click *New* and enter *demomdsvm*.

Enter *demomdsvm* as VM name.

If you plan to use GPU, select the *East US* region, otherwise any region.

Under *Authentication type* select *Password* and enter a user name and password. You will use these to access the VM.

Click *Review + Create*, then *Create*.

When the deployment is finished, open the VM in the portal and note the *Public IP address* from the *Overview* page.

## Download files to the VM from GitHub

### Option 1: Using SSH

Open an SSH session to the public IP address of the VM.

Enter

    cd notebooks
    git clone https://github.com/gszakaly/azuremldemo


### Option 2: From Jupyter Notebook

Open https://(public IP address):8000 in a browser

Accept warning about self-signed certificate.

Log in with the VM user name and password.

In towards the upper right corner of the file list select *New* and then *Python 3.6 - AzureML*

Enter the following command into the first cell and press Shift-Enter

    !git clone https://github.com/gszakaly/azuremldemo

## Run Jupyter Notebook

Open https://(public IP address):8000 in a browser

Open the /azuremldemo/Data Science Virtual Machine/Fashion-MNIST DSVM.ipynb notebook.

Beginning from the top execute each cell by clicking the *Run* button or pressing Shift-Enter.
