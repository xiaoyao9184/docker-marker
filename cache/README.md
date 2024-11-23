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

and `./cache/huggingface/hub/models--vikp--surya_layout3` like this

```
.
├── blobs
│   ├── 0a51f931c62cfc4a56f9afdaedfa96336b040a47
│   ├── 26e1ccb624958982ad55191648d53f9610cfce83b5bd9a227804a62bf3446639
│   ├── 2cd406fa7808c997daa69ef095b1992f243dadd7
│   ├── 64a74e7f804289d76c13f7aab35ad32c6071ccb41db04d8626909c84063971b4
│   ├── a6344aac8c09253b3b630fb776ae94478aa0275b
│   └── afaa751c9f40e9df6796a7c2f3d7a9a2159ccae0
├── refs
│   └── main
└── snapshots
    └── 6f4c319b213ddbe736c9fe6de87ad7dc3bbb0a1e
        ├── config.json -> ../../blobs/afaa751c9f40e9df6796a7c2f3d7a9a2159ccae0
        ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b
        ├── model.safetensors -> ../../blobs/64a74e7f804289d76c13f7aab35ad32c6071ccb41db04d8626909c84063971b4
        ├── preprocessor_config.json -> ../../blobs/2cd406fa7808c997daa69ef095b1992f243dadd7
        ├── README.md -> ../../blobs/0a51f931c62cfc4a56f9afdaedfa96336b040a47
        └── training_args.bin -> ../../blobs/26e1ccb624958982ad55191648d53f9610cfce83b5bd9a227804a62bf3446639

4 directories, 13 files
```

and `./cache/huggingface/hub/models--vikp--surya_order` like this

```
.
├── blobs
│   ├── 4566f6f099f2c8ff7426500ff4a7d84a7a8514a0
│   ├── 6b317ef99d47ee51bfa3aa47db49030f692c30c8
│   ├── a6344aac8c09253b3b630fb776ae94478aa0275b
│   ├── bb3f109ce8d6999ebfda8fbe7940ce7e68ea7e60
│   ├── cda4db4b7f886de50399b061100af28767cf2b71
│   └── d6688651c37649cc60492f18b5e6bf085f852e0f05e0543b6ca57f25fa884b4a
├── refs
│   └── main
└── snapshots
    └── 7b727d0a2c942cdc8596d186115f65c12c812bd8
        ├── config.json -> ../../blobs/4566f6f099f2c8ff7426500ff4a7d84a7a8514a0
        ├── generation_config.json -> ../../blobs/cda4db4b7f886de50399b061100af28767cf2b71
        ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b
        ├── model.safetensors -> ../../blobs/d6688651c37649cc60492f18b5e6bf085f852e0f05e0543b6ca57f25fa884b4a
        ├── preprocessor_config.json -> ../../blobs/bb3f109ce8d6999ebfda8fbe7940ce7e68ea7e60
        └── README.md -> ../../blobs/6b317ef99d47ee51bfa3aa47db49030f692c30c8

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

and `./cache/huggingface/hub/models--vikp--surya_tablerec` like this

```
.
├── blobs
│   ├── 2f525ec0be1f2e8cb257a7b3e01de3bd003f0e81
│   ├── 4f269f7454bc6161d8482c86f1e02752da76bf36
│   ├── 59a0e54bb3f1ccc8313ed1a75035435e477773ecc62cc1bb0cee0e5dc58889c8
│   ├── 5f777357fc63326274fb93cbedf4948d61a89439
│   ├── 93c190b5690dd55aac16723222a9909e2be0faec
│   ├── a6344aac8c09253b3b630fb776ae94478aa0275b
│   ├── b1610cd7faa8eaa790a69059e2686534a95f4ef8
│   ├── bc2c740bf5bdf1af8a4909cb79c69c950745725b
│   └── f9cf6e019c3303cdbfdbae10cf9d4057b65ba050
├── refs
│   └── main
└── snapshots
    └── 8bca165f81e9cee5fb382413eb23175079917d14
        ├── added_tokens.json -> ../../blobs/93c190b5690dd55aac16723222a9909e2be0faec
        ├── config.json -> ../../blobs/5f777357fc63326274fb93cbedf4948d61a89439
        ├── generation_config.json -> ../../blobs/b1610cd7faa8eaa790a69059e2686534a95f4ef8
        ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b
        ├── model.safetensors -> ../../blobs/59a0e54bb3f1ccc8313ed1a75035435e477773ecc62cc1bb0cee0e5dc58889c8
        ├── preprocessor_config.json -> ../../blobs/bc2c740bf5bdf1af8a4909cb79c69c950745725b
        ├── README.md -> ../../blobs/4f269f7454bc6161d8482c86f1e02752da76bf36
        ├── special_tokens_map.json -> ../../blobs/2f525ec0be1f2e8cb257a7b3e01de3bd003f0e81
        └── tokenizer_config.json -> ../../blobs/f9cf6e019c3303cdbfdbae10cf9d4057b65ba050

4 directories, 19 files
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
- `./cache/huggingface/hub/models--vikp--surya_layout3/snapshots/6f4c319b213ddbe736c9fe6de87ad7dc3bbb0a1e`
- `./cache/huggingface/hub/models--vikp--surya_order/snapshots/7b727d0a2c942cdc8596d186115f65c12c812bd8`
- `./cache/huggingface/hub/models--vikp--surya_rec2/snapshots/6611509b2c3a32c141703ce19adc899d9d0abf41`
- `./cache/huggingface/hub/models--vikp--surya_tablerec/snapshots/8bca165f81e9cee5fb382413eb23175079917d14`
- `./cache/huggingface/hub/models--vikp--texify/snapshots/ce49c1fe10842e78b8be61f9e762b85ac952807d`.

For more details, refer to [up@cpu-offline/docker-compose.yml](./../docker/up@cpu-offline/docker-compose.yml).


## Pre-download for offline mode

Running in online mode will automatically download the model.

install cli

```bash
pip install -U "huggingface_hub[cli]"
```

download model

```bash
huggingface-cli download vikp/surya_det3 --repo-type model --revision main --cache-dir ./cache/huggingface/hub
huggingface-cli download vikp/surya_layout3 --repo-type model --revision main --cache-dir ./cache/huggingface/hub
huggingface-cli download vikp/surya_order --repo-type model --revision main --cache-dir ./cache/huggingface/hub
huggingface-cli download vikp/surya_rec2 --repo-type model --revision main --cache-dir ./cache/huggingface/hub
huggingface-cli download vikp/surya_tablerec --repo-type model --revision main --cache-dir ./cache/huggingface/hub
huggingface-cli download vikp/texify --repo-type model --revision main --cache-dir ./cache/huggingface/hub
```