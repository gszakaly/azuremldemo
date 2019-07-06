## Create Workspace

Open *All services*.

Under *AI + machine learning* select *Machine Learning service workspaces*.

Select *Add*.

Enter *demomlservice* as name.

Under *Resource group* click *New* and enter *demomlservice*.

If you plan to use GPU, select the *East US* region, otherwise any region.

Click *Review + Create*, then *Create*.

## Create compute for training

Open the Workspace.

Under *Assets* select *Compute*.

Click *Add Compute*.

Enter *dsvmcompute* for name.

Set  *Compute type* to *Machine Learning Compute*.

Select a Virtual Machine size.

Set maximum number of nodes to *1*.

Click *Create*.

## Configure environment

If using local Jupyter Notebook, install azureml library

    pip install --upgrade azureml-sdk

In Azure Portal type *subscription* into the search box at the top and select *Subscriptions*. Note the subscription ID.

Create new file *config.json* in the same folder as the Jupyter Notebook with the following content

    {
        "subscription_id": "<azure-subscription-id>",
        "resource_group": "mldemoworkspace",
        "workspace_name": "mldemoworkspace"
    }

## Run training

Execute Jupyter Notebook *Fashion-MNIST Workspace Training*. This runs the *train.py* script on the *dsvmcompute* compute target.

Note: first run takes longer as custom Docker image is built.

## Examine training results

Open the Workspace.

Under *Assets* select *Experiments*

Select *ai-lunch-and-learn-training* and then the execution.

Under Logs select *driver_log.txt* and view the output of the *train.py* script.

Select the *Models* tab.

Check the newly created *fashion-mnist-model* model.

