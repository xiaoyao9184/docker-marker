# cache

This folder is the cache directory for Hugging Face (HF).

When using online mode, downloaded models will be cached in this folder.

For [offline mode](https://huggingface.co/docs/transformers/main/installation#offline-mode) use, please download the models in advance and specify the model directory,
such as the `surya_det3` model below.

The folder structure for `./cache/huggingface/hub/models--vikp--surya_det3` is as follows.

```
.
├── blobs
│   ├── 17579df25d3b063dedb036aaca5b495efe5088b8
│   ├── 5a2a74e413345541b7ca0db0cb1d41785649eb99fe6a1b5166aa8bd7c0a8881d
│   ├── 6d76255a802ec614336406c974998559b5cae01b112b47ec7eab1ed39b5fdb4c
│   ├── 9888778190fd6ecff72bde2ecab5b24cda345851
│   ├── a6344aac8c09253b3b630fb776ae94478aa0275b
│   └── ac9b1b39818223e631ec9982956df6d65b33f082
├── refs
│   └── main
└── snapshots
    └── 467ee9ec33e6e6c5f73e57dbc1415b14032f5b95
        ├── config.json -> ../../blobs/9888778190fd6ecff72bde2ecab5b24cda345851
        ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b
        ├── model.safetensors -> ../../blobs/5a2a74e413345541b7ca0db0cb1d41785649eb99fe6a1b5166aa8bd7c0a8881d
        ├── preprocessor_config.json -> ../../blobs/17579df25d3b063dedb036aaca5b495efe5088b8
        ├── README.md -> ../../blobs/ac9b1b39818223e631ec9982956df6d65b33f082
        └── training_args.bin -> ../../blobs/6d76255a802ec614336406c974998559b5cae01b112b47ec7eab1ed39b5fdb4c

4 directories, 13 files
```

and `./cache/huggingface/hub/models--vikp--surya_rec2` like this

```
.
├── blobs
│   ├── 2f525ec0be1f2e8cb257a7b3e01de3bd003f0e81
│   ├── 31bdd446acbf8a47ea46d7d0a4998f145f0cc75a
│   ├── 5497e8690cfe93cbedec7efaf91f6ac734496ac8
│   ├── 93c190b5690dd55aac16723222a9909e2be0faec
│   ├── 9a75b64cbeaed06820559bcda4e12c1235de62b5bce787d57cf56a9c3a7123d1
│   ├── a6344aac8c09253b3b630fb776ae94478aa0275b
│   ├── a83ef0a8114bd50cc650e08a9738c0f6345f5186
│   ├── dd34282c30833587a799d334d44a637694d41c8e
│   └── e237701f4293e736f74d2c968582935590107034
├── refs
│   └── main
└── snapshots
    └── 6611509b2c3a32c141703ce19adc899d9d0abf41
        ├── added_tokens.json -> ../../blobs/93c190b5690dd55aac16723222a9909e2be0faec
        ├── config.json -> ../../blobs/5497e8690cfe93cbedec7efaf91f6ac734496ac8
        ├── generation_config.json -> ../../blobs/e237701f4293e736f74d2c968582935590107034
        ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b
        ├── model.safetensors -> ../../blobs/9a75b64cbeaed06820559bcda4e12c1235de62b5bce787d57cf56a9c3a7123d1
        ├── preprocessor_config.json -> ../../blobs/dd34282c30833587a799d334d44a637694d41c8e
        ├── README.md -> ../../blobs/a83ef0a8114bd50cc650e08a9738c0f6345f5186
        ├── special_tokens_map.json -> ../../blobs/2f525ec0be1f2e8cb257a7b3e01de3bd003f0e81
        └── tokenizer_config.json -> ../../blobs/31bdd446acbf8a47ea46d7d0a4998f145f0cc75a

4 directories, 19 files
```

and `./cache/huggingface/hub/models--datalab-to--surya_tablerec` like this

```
.
.
├── blobs
│   ├── 38da0234ebdf63bed033dba22ed1005e0734b9f0-gzip
│   ├── 3c7c6a10d0d6f251612d9fbc86faab06d66fd918
│   ├── 8529105dadb286a81a32ffaf62583dbc-10
│   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│   └── e6c9b7e8b7850a7c02ad3895985f3e86d69256d5-gzip
└── snapshots
    └── 7327dac38c300b2f6cd0501ebc2347dd3ef7fcf2
        ├── config.json -> ../../blobs/38da0234ebdf63bed033dba22ed1005e0734b9f0-gzip
        ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
        ├── model.safetensors -> ../../blobs/8529105dadb286a81a32ffaf62583dbc-10
        ├── preprocessor_config.json -> ../../blobs/e6c9b7e8b7850a7c02ad3895985f3e86d69256d5-gzip
        └── README.md -> ../../blobs/3c7c6a10d0d6f251612d9fbc86faab06d66fd918

4 directories, 10 files
```

and `./cache/huggingface/hub/models--datalab-to--surya_layout` like this


```
.
├── blobs
│   ├── 3890b5c4361d8c355b18efcbc083d80b-10
│   ├── 5551e790c7d99f076fb8ff17b38339138e4fc543
│   ├── 776774696986893ca5eb478899ea9d06c20435c5
│   ├── a6344aac8c09253b3b630fb776ae94478aa0275b
│   └── c305af17d2fcaf52c00b125a2dfabfbe16e71454
├── refs
│   └── main
└── snapshots
    └── 7ac8e390226ee5fa2125dd303d827f79d31d1a1f
        ├── config.json -> ../../blobs/5551e790c7d99f076fb8ff17b38339138e4fc543
        ├── model.safetensors -> ../../blobs/3890b5c4361d8c355b18efcbc083d80b-10
        ├── preprocessor_config.json -> ../../blobs/776774696986893ca5eb478899ea9d06c20435c5
        └── README.md -> ../../blobs/c305af17d2fcaf52c00b125a2dfabfbe16e71454

5 directories, 10 files
```

and `./cache/huggingface/hub/models--datalab-to--ocr_error_detection` like this


```
.
├── blobs
│   ├── 21f54a4b56685f29358f3a8de1f5b8d827357d07
│   ├── 9856c52ab99c8f7435bef6bf6e4c8a86a2594187
│   ├── 9bbecc17cabbcbd3112c14d6982b51403b264bfa
│   ├── a6344aac8c09253b3b630fb776ae94478aa0275b
│   ├── c305af17d2fcaf52c00b125a2dfabfbe16e71454
│   ├── cd3c57f2e967aad6a020decd1c1c41be-10
│   ├── e837bab60a5d204e29622d127c2dafe508aa0731
│   └── f4a46fa248690b0b2adc680e845ec8fd491eb24c
├── refs
│   └── main
└── snapshots
    └── c1cbda3757670fd520553eaa5197656d331de414
        ├── config.json -> ../../blobs/9856c52ab99c8f7435bef6bf6e4c8a86a2594187
        ├── model.safetensors -> ../../blobs/cd3c57f2e967aad6a020decd1c1c41be-10
        ├── README.md -> ../../blobs/c305af17d2fcaf52c00b125a2dfabfbe16e71454
        ├── special_tokens_map.json -> ../../blobs/9bbecc17cabbcbd3112c14d6982b51403b264bfa
        ├── tokenizer_config.json -> ../../blobs/f4a46fa248690b0b2adc680e845ec8fd491eb24c
        ├── tokenizer.json -> ../../blobs/21f54a4b56685f29358f3a8de1f5b8d827357d07
        └── vocab.txt -> ../../blobs/e837bab60a5d204e29622d127c2dafe508aa0731

5 directories, 16 files
```

and `./cache/huggingface/hub/models--vikp--texify` like this

```
.
├── blobs
│   ├── 1b3717b4b654d773f5f79c93cdc994e18dd9d0ee574ad5f9bb3f8c028b79e7b3
│   ├── 4c48133aabc13f4e5f04badd8214b294a033f85b
│   ├── 614a553895a796faf884b140cae23a04c10eda6b
│   ├── 75dad5a63711d242ad16d0e2a11e194fa073fcce
│   ├── a6344aac8c09253b3b630fb776ae94478aa0275b
│   ├── a782b2f1cdab4d0bacb2dc0f85d02c4b1e31f0bd
│   ├── aa6fa677ace60c9b55199d5db22a1dce5198c5ac
│   ├── c4eed27b2bbeb493d7fbba31feda6af5c7527246a35a96d49eaa1010f9c7e9af
│   ├── cb0af56b5c3710c1f721270799366b1ac33ea76a
│   ├── cb9e3dce4c326195d08fc3dd0f7e2eee1da8595c847bf4c1a9c78b7a82d47e2d
│   ├── ea462a33e5f84b37a56e99a304aec22a89d53670
│   └── fa625711098f8cd0b355710ff6a95c894b073d62
├── refs
│   └── main
└── snapshots
    └── ce49c1fe10842e78b8be61f9e762b85ac952807d
        ├── added_tokens.json -> ../../blobs/ea462a33e5f84b37a56e99a304aec22a89d53670
        ├── config.json -> ../../blobs/614a553895a796faf884b140cae23a04c10eda6b
        ├── generation_config.json -> ../../blobs/4c48133aabc13f4e5f04badd8214b294a033f85b
        ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b
        ├── model.safetensors -> ../../blobs/c4eed27b2bbeb493d7fbba31feda6af5c7527246a35a96d49eaa1010f9c7e9af
        ├── preprocessor_config.json -> ../../blobs/aa6fa677ace60c9b55199d5db22a1dce5198c5ac
        ├── README.md -> ../../blobs/fa625711098f8cd0b355710ff6a95c894b073d62
        ├── sentencepiece.bpe.model -> ../../blobs/cb9e3dce4c326195d08fc3dd0f7e2eee1da8595c847bf4c1a9c78b7a82d47e2d
        ├── special_tokens_map.json -> ../../blobs/a782b2f1cdab4d0bacb2dc0f85d02c4b1e31f0bd
        ├── tokenizer_config.json -> ../../blobs/75dad5a63711d242ad16d0e2a11e194fa073fcce
        ├── tokenizer.json -> ../../blobs/cb0af56b5c3710c1f721270799366b1ac33ea76a
        └── training_args.bin -> ../../blobs/1b3717b4b654d773f5f79c93cdc994e18dd9d0ee574ad5f9bb3f8c028b79e7b3

4 directories, 25 files
```

It will use
- `./cache/huggingface/hub/models--vikp--surya_det3/snapshots/467ee9ec33e6e6c5f73e57dbc1415b14032f5b95`
- `./cache/huggingface/hub/models--vikp--surya_rec2/snapshots/6611509b2c3a32c141703ce19adc899d9d0abf41`
- `./cache/huggingface/hub/models--datalab-to--surya_tablerec/snapshots/7327dac38c300b2f6cd0501ebc2347dd3ef7fcf2`
- `./cache/huggingface/hub/models--vikp--texify/snapshots/ce49c1fe10842e78b8be61f9e762b85ac952807d`
- `./cache/huggingface/hub/models--datalab-to--surya_layout/snapshots/7ac8e390226ee5fa2125dd303d827f79d31d1a1f`
- `./cache/huggingface/hub/models--datalab-to--ocr_error_detection/snapshots/c1cbda3757670fd520553eaa5197656d331de414`

For more details, refer to [up@cpu-offline/docker-compose.yml](./../docker/up@cpu-offline/docker-compose.yml).


## Pre-download for offline mode

Running in online mode will automatically download the model.

install cli

```bash
pip install -U "huggingface_hub[cli]"
```

download model

```bash
huggingface-cli download vikp/surya_det3 --repo-type model --revision 467ee9ec33e6e6c5f73e57dbc1415b14032f5b95 --cache-dir ./cache/huggingface/hub
huggingface-cli download vikp/surya_rec2 --repo-type 6611509b2c3a32c141703ce19adc899d9d0abf41 --revision main --cache-dir ./cache/huggingface/hub
huggingface-cli download datalab-to/surya_tablerec --repo-type model --revision 7327dac38c300b2f6cd0501ebc2347dd3ef7fcf2 --cache-dir ./cache/huggingface/hub
huggingface-cli download vikp/texify --repo-type model --revision ce49c1fe10842e78b8be61f9e762b85ac952807d --cache-dir ./cache/huggingface/hub
huggingface-cli download datalab-to/surya_layout --repo-type model --revision 7ac8e390226ee5fa2125dd303d827f79d31d1a1f --cache-dir ./cache/huggingface/hub
huggingface-cli download datalab-to/ocr_error_detection --repo-type model --revision c1cbda3757670fd520553eaa5197656d331de414 --cache-dir ./cache/huggingface/hub
```