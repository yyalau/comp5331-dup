# COMP 5331 Group Project

## General Information

**Title:** Causal Inference via Style Transfer for Out-of-Distribution Generalisation

**Project Type:** Implementation

**Group Number:** 13

**Members:**

| Student ID | Student Name | Contribution |
| ---------- | ------------ | ------------ |
| 20504741 | LEUNG, Tin Long | Data visualization / traineval |
| 20583797 | TANG, Zheng | Main framework |
| 20596201 | LAU, Ying Yee Ava | NST model |
| 20607969 | WONG, Chi Ho | Classifier model |
| 20942785 | BAHARI, Maral | Main framework |
| 20943026 | BA SOWID, Badr Saleh Abdullah | Data config / preprocessing |

## Installation

### Requirements

- [Python](https://www.python.org/) 3.10
- [CUDA](https://developer.nvidia.com/cuda-toolkit-archive) 11.8+

### Setup

1. Activate a virtual Python environment (e.g. [conda](https://docs.conda.io/en/latest/)).
2. Install the dependencies.
```sh
python -m pip install torch==2.1.* torchvision==0.16.* torchaudio==2.1.* --index-url https://download.pytorch.org/whl/cu118
python -m pip install -r requirements.txt
```

## Usage

### Baseline Method

1. Train a standard ERM (Empirical Risk Minimization) classifier:
```sh
# By default, checkpoints are stored in `./experiments/erm`
python run_erm.py [OPTIONS]
```

### Proposed Method

1. *(Optional)* Train a NST (Neural Style Transfer) model:
```sh
# By default, checkpoints are stored in `./experiments/nst`
python run_nst.py [OPTIONS]
```

2. Train a FAST (Front-door Adjustment via Neural Style Transfer) classifier:
```sh
# You can use the NST model from Step 1 or download a pretrained one
# By default, checkpoints are stored in `./experiments/fast`
python run_fast.py [OPTIONS]
```

## References

Our code is based on the GitHub repository for the following papers:
- [Causal Inference via Style Transfer for Out-of-distribution Generalisation](https://github.com/nktoan/Causal-Inference-via-Style-Transfer-for-OOD-Generalisation)
- [AdaIN](https://github.com/MAlberts99/PyTorch-AdaIN-StyleTransfer)
- [Image Transfer Network](https://github.com/zuotengxu/Image-Neural-Style-Transfer-With-Preserving-the-Salient-Regions)
- [Vision Transformer](https://github.com/google-research/vision_transformer)
