from sagemaker.pytorch import PyTorchModel
import sagemaker

role = "<your-iam-role>"
sagemaker_session = sagemaker.Session()

model = PyTorchModel(
    model_data="s3://my-bucket/bert-cnn-model.tar.gz",
    role=role,
    entry_point="inference.py",
    framework_version="1.12",
    py_version="py38"
)

# Deploy to a managed endpoint
predictor = model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.xlarge"
)