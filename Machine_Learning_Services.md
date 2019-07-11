## Create Workspace

Open https://portal.azure.com in a browser.

Open *All services*.

Under *AI + machine learning* select *Machine Learning service workspaces*.

Select *Add*.

Enter *demomlservice* as workspace name.

Under *Resource group* click *New* and enter *demomlservice*.

If you plan to use GPU, select the *East US* region, otherwise any region.

Click *Review + Create*, then *Create*.

## Create compute for training

Open the Workspace.

Under *Assets* select *Compute*.

Click *Add Compute*.

Enter *dsvmcompute* for name.

Set  *Compute type* to *Machine Learning Compute*.

Click *Choose Virtual machine size* and select *Standard_DS2_v2* for a general purpose VM.

Set maximum number of nodes to *1*.

Click *Create*.

## Configure environment

If using local Jupyter Notebook, install azureml library

    pip install azureml-sdk

If not using the DSVM from the previous excercise, clone the https://github.com/gszakaly/azuremldemo repository.

On the Overview page of the workspace click *Download JSON configuration*.

Save/upload the *config.json* file in the same folder as the Jupyter Notebook *Fashion-MNIST Workspace Training*.

## Run training

Execute Jupyter Notebook *azuremldemo/Machine Learning Services/Fashion-MNIST Workspace Training*. This runs the *train.py* script on the *dsvmcompute* compute target.

If running in DSVM use the *Python 3.6 - AzureML* kernel. To select it, open the Notebook and open *Kernel*, then *Change Kernel*, then select *Python 3.6 - AzureML*.

When instructed, navigate to https://microsoft.com/devicelogin on a separate tab and enter code shown.

Where instructed, wait until the training is completed, before progressing to the next cell.

Note: first run takes longer as custom Docker image is built.

## Examine training results

Open the Workspace.

Under *Assets* select *Experiments*

Select *ai-lunch-and-learn-training* and then the execution.

Under Logs select *driver_log.txt* and view the output of the *train.py* script.

Select the *Models* tab.

Check the newly created *fashion-mnist-model* model.

## Deploy model as Azure Container Instance

Execute all cells in the Jupyter Notebook */azuremldemo/Machine Learning Services/Fashion-MNIST Workspace Deployment.ipynb*.

If running in DSVM use the *Python 3.6 - AzureML* kernel.

## Test deployed model

POST to the URL returned by the last cell of the *Fashion-MNIST Workspace Deployment.ipynb* notebook. Use the JSON files under */azuremldemo/Test Requests* as request body. Set the *Content-Type* header to *application/json*.