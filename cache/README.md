# cache

This folder is the cache directory for Hugging Face (HF) and Surya models S3 bucket.

When using online mode, downloaded models will be cached in this folder.

For [offline mode](https://huggingface.co/docs/transformers/main/installation#offline-mode) use, please download the models in advance and specify the model directory.


## Directory structures

**There are currently two directory structures:**
- The Huggingface CLI cache structure
- The Surya S3 bucket download structure

Starting from Marker version 1.5.4, the Surya S3 bucket structure is used by default.

### Huggingface CLI cache structure

use this command `tree -a ./cache/huggingface/hub`

```
./cache/huggingface/hub
├── .locks
│   ├── models--datalab-to--inline_math_det0
│   │   ├── 15937d4ae6bf71a1bbe36715fa9aeea2d56c3a7c.lock
│   │   ├── 1674f2a5253af7f3bcb38eb7dbe5f1cf3ed1dcb3-gzip.lock
│   │   ├── 310f06a4fe98b66f90fcecd2776d9699a6641993.lock
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip.lock
│   │   └── cf2efdb51bd3f5b383b5dbe035d3a8c6-10.lock
│   ├── models--datalab-to--ocr_error_detection
│   │   ├── 21f54a4b56685f29358f3a8de1f5b8d827357d07-gzip.lock
│   │   ├── 9856c52ab99c8f7435bef6bf6e4c8a86a2594187-gzip.lock
│   │   ├── 9bbecc17cabbcbd3112c14d6982b51403b264bfa-gzip.lock
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip.lock
│   │   ├── c305af17d2fcaf52c00b125a2dfabfbe16e71454.lock
│   │   ├── cd3c57f2e967aad6a020decd1c1c41be-10.lock
│   │   ├── e837bab60a5d204e29622d127c2dafe508aa0731-gzip.lock
│   │   └── f4a46fa248690b0b2adc680e845ec8fd491eb24c-gzip.lock
│   ├── models--datalab-to--surya_layout
│   │   ├── 3890b5c4361d8c355b18efcbc083d80b-10.lock
│   │   ├── 5551e790c7d99f076fb8ff17b38339138e4fc543-gzip.lock
│   │   ├── 776774696986893ca5eb478899ea9d06c20435c5.lock
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip.lock
│   │   └── c305af17d2fcaf52c00b125a2dfabfbe16e71454.lock
│   ├── models--datalab-to--surya_tablerec
│   │   ├── 38da0234ebdf63bed033dba22ed1005e0734b9f0-gzip.lock
│   │   ├── 3c7c6a10d0d6f251612d9fbc86faab06d66fd918.lock
│   │   ├── 8529105dadb286a81a32ffaf62583dbc-10.lock
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip.lock
│   │   └── e6c9b7e8b7850a7c02ad3895985f3e86d69256d5-gzip.lock
│   ├── models--datalab-to--texify
│   │   ├── 0b7eef4d4e38242a8bfe86b25350ee57a80ddea2-gzip.lock
│   │   ├── 1c7a55edfe48b2b661b042bf711fbfce-10.lock
│   │   ├── 38d90143fbee233a4f7124e5323b9564de233224-gzip.lock
│   │   ├── 5e12d9ba900b47f9ffa293b89737baa294699859.lock
│   │   ├── 80cf0856476a03804ea7139a7ded72575f3f38c6-gzip.lock
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip.lock
│   │   ├── a782b2f1cdab4d0bacb2dc0f85d02c4b1e31f0bd-gzip.lock
│   │   ├── e3cd24912053c61b0331779b976df959-10.lock
│   │   └── fbed506ad438e179c130257fabd67cb49c932793-gzip.lock
│   ├── models--vikp--surya_det3
│   │   ├── 17579df25d3b063dedb036aaca5b495efe5088b8-gzip.lock
│   │   ├── 9888778190fd6ecff72bde2ecab5b24cda345851-gzip.lock
│   │   ├── a2ece6e1302dc18542313b2ffe3c7bf0-10.lock
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip.lock
│   │   ├── ac9b1b39818223e631ec9982956df6d65b33f082.lock
│   │   └── afcb9fff8bb63b61a30c13185cbf662b-10.lock
│   └── models--vikp--surya_rec2
│       ├── 2f525ec0be1f2e8cb257a7b3e01de3bd003f0e81-gzip.lock
│       ├── 31bdd446acbf8a47ea46d7d0a4998f145f0cc75a-gzip.lock
│       ├── 5497e8690cfe93cbedec7efaf91f6ac734496ac8-gzip.lock
│       ├── 86c018e1634a8562974ad5d115034731-10.lock
│       ├── 93c190b5690dd55aac16723222a9909e2be0faec-gzip.lock
│       ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip.lock
│       ├── a83ef0a8114bd50cc650e08a9738c0f6345f5186.lock
│       ├── dd34282c30833587a799d334d44a637694d41c8e-gzip.lock
│       └── e237701f4293e736f74d2c968582935590107034.lock
├── models--datalab-to--inline_math_det0
│   ├── blobs
│   │   ├── 15937d4ae6bf71a1bbe36715fa9aeea2d56c3a7c
│   │   ├── 1674f2a5253af7f3bcb38eb7dbe5f1cf3ed1dcb3-gzip
│   │   ├── 310f06a4fe98b66f90fcecd2776d9699a6641993
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│   │   └── cf2efdb51bd3f5b383b5dbe035d3a8c6-10
│   ├── refs
│   │   └── main
│   └── snapshots
│       └── 75aafc7aa3d494ece6496d28038c91f0d2518a43
│           ├── config.json -> ../../blobs/1674f2a5253af7f3bcb38eb7dbe5f1cf3ed1dcb3-gzip
│           ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│           ├── model.safetensors -> ../../blobs/cf2efdb51bd3f5b383b5dbe035d3a8c6-10
│           ├── preprocessor_config.json -> ../../blobs/15937d4ae6bf71a1bbe36715fa9aeea2d56c3a7c
│           └── README.md -> ../../blobs/310f06a4fe98b66f90fcecd2776d9699a6641993
├── models--datalab-to--ocr_error_detection
│   ├── blobs
│   │   ├── 21f54a4b56685f29358f3a8de1f5b8d827357d07-gzip
│   │   ├── 9856c52ab99c8f7435bef6bf6e4c8a86a2594187-gzip
│   │   ├── 9bbecc17cabbcbd3112c14d6982b51403b264bfa-gzip
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│   │   ├── c305af17d2fcaf52c00b125a2dfabfbe16e71454
│   │   ├── cd3c57f2e967aad6a020decd1c1c41be-10
│   │   ├── e837bab60a5d204e29622d127c2dafe508aa0731-gzip
│   │   └── f4a46fa248690b0b2adc680e845ec8fd491eb24c-gzip
│   ├── refs
│   │   └── main
│   └── snapshots
│       └── c1cbda3757670fd520553eaa5197656d331de414
│           ├── config.json -> ../../blobs/9856c52ab99c8f7435bef6bf6e4c8a86a2594187-gzip
│           ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│           ├── model.safetensors -> ../../blobs/cd3c57f2e967aad6a020decd1c1c41be-10
│           ├── README.md -> ../../blobs/c305af17d2fcaf52c00b125a2dfabfbe16e71454
│           ├── special_tokens_map.json -> ../../blobs/9bbecc17cabbcbd3112c14d6982b51403b264bfa-gzip
│           ├── tokenizer_config.json -> ../../blobs/f4a46fa248690b0b2adc680e845ec8fd491eb24c-gzip
│           ├── tokenizer.json -> ../../blobs/21f54a4b56685f29358f3a8de1f5b8d827357d07-gzip
│           └── vocab.txt -> ../../blobs/e837bab60a5d204e29622d127c2dafe508aa0731-gzip
├── models--datalab-to--surya_layout
│   ├── blobs
│   │   ├── 3890b5c4361d8c355b18efcbc083d80b-10
│   │   ├── 5551e790c7d99f076fb8ff17b38339138e4fc543-gzip
│   │   ├── 776774696986893ca5eb478899ea9d06c20435c5
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│   │   └── c305af17d2fcaf52c00b125a2dfabfbe16e71454
│   ├── refs
│   │   └── main
│   └── snapshots
│       └── 7ac8e390226ee5fa2125dd303d827f79d31d1a1f
│           ├── config.json -> ../../blobs/5551e790c7d99f076fb8ff17b38339138e4fc543-gzip
│           ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│           ├── model.safetensors -> ../../blobs/3890b5c4361d8c355b18efcbc083d80b-10
│           ├── preprocessor_config.json -> ../../blobs/776774696986893ca5eb478899ea9d06c20435c5
│           └── README.md -> ../../blobs/c305af17d2fcaf52c00b125a2dfabfbe16e71454
├── models--datalab-to--surya_tablerec
│   ├── blobs
│   │   ├── 38da0234ebdf63bed033dba22ed1005e0734b9f0-gzip
│   │   ├── 3c7c6a10d0d6f251612d9fbc86faab06d66fd918
│   │   ├── 8529105dadb286a81a32ffaf62583dbc-10
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│   │   └── e6c9b7e8b7850a7c02ad3895985f3e86d69256d5-gzip
│   ├── refs
│   │   └── main
│   └── snapshots
│       └── 7327dac38c300b2f6cd0501ebc2347dd3ef7fcf2
│           ├── config.json -> ../../blobs/38da0234ebdf63bed033dba22ed1005e0734b9f0-gzip
│           ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│           ├── model.safetensors -> ../../blobs/8529105dadb286a81a32ffaf62583dbc-10
│           ├── preprocessor_config.json -> ../../blobs/e6c9b7e8b7850a7c02ad3895985f3e86d69256d5-gzip
│           └── README.md -> ../../blobs/3c7c6a10d0d6f251612d9fbc86faab06d66fd918
├── models--datalab-to--texify
│   ├── blobs
│   │   ├── 0b7eef4d4e38242a8bfe86b25350ee57a80ddea2-gzip
│   │   ├── 1c7a55edfe48b2b661b042bf711fbfce-10
│   │   ├── 38d90143fbee233a4f7124e5323b9564de233224-gzip
│   │   ├── 5e12d9ba900b47f9ffa293b89737baa294699859
│   │   ├── 80cf0856476a03804ea7139a7ded72575f3f38c6-gzip
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│   │   ├── a782b2f1cdab4d0bacb2dc0f85d02c4b1e31f0bd-gzip
│   │   ├── e3cd24912053c61b0331779b976df959-10
│   │   └── fbed506ad438e179c130257fabd67cb49c932793-gzip
│   ├── refs
│   │   └── main
│   └── snapshots
│       └── 8f1d761762b3e977e9e62cebfca487d489556abc
│           ├── config.json -> ../../blobs/80cf0856476a03804ea7139a7ded72575f3f38c6-gzip
│           ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│           ├── model.safetensors -> ../../blobs/e3cd24912053c61b0331779b976df959-10
│           ├── preprocessor_config.json -> ../../blobs/0b7eef4d4e38242a8bfe86b25350ee57a80ddea2-gzip
│           ├── README.md -> ../../blobs/5e12d9ba900b47f9ffa293b89737baa294699859
│           ├── special_tokens_map.json -> ../../blobs/a782b2f1cdab4d0bacb2dc0f85d02c4b1e31f0bd-gzip
│           ├── tokenizer_config.json -> ../../blobs/38d90143fbee233a4f7124e5323b9564de233224-gzip
│           ├── tokenizer.json -> ../../blobs/fbed506ad438e179c130257fabd67cb49c932793-gzip
│           └── training_args.bin -> ../../blobs/1c7a55edfe48b2b661b042bf711fbfce-10
├── models--vikp--surya_det3
│   ├── blobs
│   │   ├── 17579df25d3b063dedb036aaca5b495efe5088b8-gzip
│   │   ├── 9888778190fd6ecff72bde2ecab5b24cda345851-gzip
│   │   ├── a2ece6e1302dc18542313b2ffe3c7bf0-10
│   │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│   │   ├── ac9b1b39818223e631ec9982956df6d65b33f082
│   │   └── afcb9fff8bb63b61a30c13185cbf662b-10
│   ├── refs
│   │   └── main
│   └── snapshots
│       └── 467ee9ec33e6e6c5f73e57dbc1415b14032f5b95
│           ├── config.json -> ../../blobs/9888778190fd6ecff72bde2ecab5b24cda345851-gzip
│           ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
│           ├── model.safetensors -> ../../blobs/afcb9fff8bb63b61a30c13185cbf662b-10
│           ├── preprocessor_config.json -> ../../blobs/17579df25d3b063dedb036aaca5b495efe5088b8-gzip
│           ├── README.md -> ../../blobs/ac9b1b39818223e631ec9982956df6d65b33f082
│           └── training_args.bin -> ../../blobs/a2ece6e1302dc18542313b2ffe3c7bf0-10
└── models--vikp--surya_rec2
    ├── blobs
    │   ├── 2f525ec0be1f2e8cb257a7b3e01de3bd003f0e81-gzip
    │   ├── 31bdd446acbf8a47ea46d7d0a4998f145f0cc75a-gzip
    │   ├── 5497e8690cfe93cbedec7efaf91f6ac734496ac8-gzip
    │   ├── 86c018e1634a8562974ad5d115034731-10
    │   ├── 93c190b5690dd55aac16723222a9909e2be0faec-gzip
    │   ├── a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
    │   ├── a83ef0a8114bd50cc650e08a9738c0f6345f5186
    │   ├── dd34282c30833587a799d334d44a637694d41c8e-gzip
    │   └── e237701f4293e736f74d2c968582935590107034
    ├── refs
    │   └── main
    └── snapshots
        └── 6611509b2c3a32c141703ce19adc899d9d0abf41
            ├── added_tokens.json -> ../../blobs/93c190b5690dd55aac16723222a9909e2be0faec-gzip
            ├── config.json -> ../../blobs/5497e8690cfe93cbedec7efaf91f6ac734496ac8-gzip
            ├── generation_config.json -> ../../blobs/e237701f4293e736f74d2c968582935590107034
            ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b-gzip
            ├── model.safetensors -> ../../blobs/86c018e1634a8562974ad5d115034731-10
            ├── preprocessor_config.json -> ../../blobs/dd34282c30833587a799d334d44a637694d41c8e-gzip
            ├── README.md -> ../../blobs/a83ef0a8114bd50cc650e08a9738c0f6345f5186
            ├── special_tokens_map.json -> ../../blobs/2f525ec0be1f2e8cb257a7b3e01de3bd003f0e81-gzip
            └── tokenizer_config.json -> ../../blobs/31bdd446acbf8a47ea46d7d0a4998f145f0cc75a-gzip
```

### Surya S3 bucket download structure

use this command `tree -a ./cache/datalab/models`

```
./cache/datalab/models
├── inline_math_detection
│   └── 2025_02_18
│       ├── config.json
│       ├── .gitattributes
│       ├── manifest.json
│       ├── model.safetensors
│       ├── preprocessor_config.json
│       └── README.md
├── layout
│   └── 2025_02_18
│       ├── config.json
│       ├── .gitattributes
│       ├── manifest.json
│       ├── model.safetensors
│       ├── preprocessor_config.json
│       └── README.md
├── ocr_error_detection
│   └── 2025_02_18
│       ├── config.json
│       ├── .gitattributes
│       ├── manifest.json
│       ├── model.safetensors
│       ├── README.md
│       ├── special_tokens_map.json
│       ├── tokenizer_config.json
│       ├── tokenizer.json
│       └── vocab.txt
├── table_recognition
│   └── 2025_02_18
│       ├── config.json
│       ├── .gitattributes
│       ├── manifest.json
│       ├── model.safetensors
│       ├── preprocessor_config.json
│       └── README.md
├── texify
│   └── 2025_02_18
│       ├── config.json
│       ├── .gitattributes
│       ├── manifest.json
│       ├── model.safetensors
│       ├── preprocessor_config.json
│       ├── README.md
│       ├── special_tokens_map.json
│       ├── tokenizer_config.json
│       ├── tokenizer.json
│       └── training_args.bin
├── text_detection
│   └── 2025_02_18
│       ├── config.json
│       ├── .gitattributes
│       ├── manifest.json
│       ├── model.safetensors
│       ├── preprocessor_config.json
│       ├── README.md
│       └── training_args.bin
└── text_recognition
    └── 2025_02_18
        ├── added_tokens.json
        ├── config.json
        ├── generation_config.json
        ├── .gitattributes
        ├── manifest.json
        ├── model.safetensors
        ├── preprocessor_config.json
        ├── README.md
        ├── special_tokens_map.json
        └── tokenizer_config.json
```


## Version used

if Marker < 1.5.4, it will use

- `./cache/huggingface/hub/models--vikp--surya_det3/snapshots/467ee9ec33e6e6c5f73e57dbc1415b14032f5b95`
- `./cache/huggingface/hub/models--vikp--surya_rec2/snapshots/6611509b2c3a32c141703ce19adc899d9d0abf41`
- `./cache/huggingface/hub/models--datalab-to--surya_tablerec/snapshots/7327dac38c300b2f6cd0501ebc2347dd3ef7fcf2`
- `./cache/huggingface/hub/models--datalab-to--texify/snapshots/8f1d761762b3e977e9e62cebfca487d489556abc`
- `./cache/huggingface/hub/models--datalab-to--surya_layout/snapshots/7ac8e390226ee5fa2125dd303d827f79d31d1a1f`
- `./cache/huggingface/hub/models--datalab-to--ocr_error_detection/snapshots/c1cbda3757670fd520553eaa5197656d331de414`
- `./cache/huggingface/hub/models--datalab-to--inline_math_det0/snapshots/75aafc7aa3d494ece6496d28038c91f0d2518a43`

if Marker >= 1.5.4, it will use

- `./cache/datalab/models/text_detection/2025_02_18`
- `./cache/datalab/models/text_recognition/2025_02_18`
- `./cache/datalab/models/table_recognition/2025_02_18`
- `./cache/datalab/models/texify/2025_02_18`
- `./cache/datalab/models/layout/2025_02_18`
- `./cache/datalab/models/ocr_error_detection/2025_02_18`
- `./cache/datalab/models/inline_math_detection/2025_02_18`


### diff of Huggingface model and Surya S3 model

you can use `diff` command to make sure the model is the same

```bash
diff -qr ./cache/huggingface/hub/models--datalab-to--inline_math_det0/snapshots/75aafc7aa3d494ece6496d28038c91f0d2518a43 ./cache/datalab/models/inline_math_detection/2025_02_18
```

| huggingface model name | huggingface model version | surya s3 model name | surya s3 model version |
| --- | --- | --- | --- |
| vikp/surya_det3 | 467ee9ec33e6e6c5f73e57dbc1415b14032f5b95 | text_detection | 2025_02_18 |
| vikp/surya_rec2 | 6611509b2c3a32c141703ce19adc899d9d0abf41 | text_recognition | 2025_02_18 |
| datalab-to/surya_tablerec | 7327dac38c300b2f6cd0501ebc2347dd3ef7fcf2 | table_recognition | 2025_02_18 |
| datalab-to/texify | 8f1d761762b3e977e9e62cebfca487d489556abc | texify | 2025_02_18 |
| datalab-to/surya_layout | 7ac8e390226ee5fa2125dd303d827f79d31d1a1f | layout | 2025_02_18 |
| datalab-to/ocr_error_detection | c1cbda3757670fd520553eaa5197656d331de414 | ocr_error_detection | 2025_02_18 |
| datalab-to/inline_math_det0 | 75aafc7aa3d494ece6496d28038c91f0d2518a43 | inline_math_detection | 2025_02_18 |

| huggingface model name | huggingface model version | surya s3 model name | surya s3 model version |
| --- | --- | --- | --- |
| xiaoyao9184/surya_text_detection | 2025_05_07 | text_detection | 2025_05_07 |
| xiaoyao9184/surya_text_recognition | 2025_05_16 | text_recognition | 2025_05_16 |
| xiaoyao9184/surya_text_recognition | 2025_08_01 | text_recognition | 2025_08_01 |
| xiaoyao9184/surya_text_recognition | 2025_08_04 | text_recognition | 2025_08_04 |
| xiaoyao9184/surya_text_recognition | 2025_08_08 | text_recognition | 2025_08_08 |
| xiaoyao9184/surya_text_recognition | 2025_08_12 | text_recognition | 2025_08_12 |
| xiaoyao9184/surya_text_recognition | 2025_08_29 | text_recognition | 2025_08_29 |
| xiaoyao9184/surya_table_recognition | 2025_02_18 | table_recognition | 2025_02_18 |
| xiaoyao9184/surya_texify | 2025_02_18 | texify | 2025_02_18 |
| xiaoyao9184/surya_layout | 2025_02_18 | layout | 2025_02_18 |
| xiaoyao9184/surya_ocr_error_detection | 2025_02_18 | ocr_error_detection | 2025_02_18 |
| xiaoyao9184/surya_inline_math_detection | 2025_02_24 | inline_math_detection | 2025_02_24 |

You can specify the model path to Marker via an environment variable,
which allows you to store the model using any directory structure.
For more details, refer to [up@cpu-offline/docker-compose.yml](./../docker/up@cpu-offline/docker-compose.yml).


## Pre-download for offline mode

Running in online mode will automatically download the model.

### use huggingface-cli

install cli

```bash
pip install -U "huggingface_hub[cli]"
```

download model

```bash
huggingface-cli download xiaoyao9184/surya_text_detection --repo-type model --revision 2025_05_07 --local-dir ./cache/datalab/models/text_detection/2025_05_07
huggingface-cli download xiaoyao9184/surya_text_recognition --repo-type model --revision 2025_08_29 --local-dir ./cache/datalab/models/text_recognition/2025_08_29
huggingface-cli download xiaoyao9184/surya_table_recognition --repo-type model --revision 2025_02_18 --local-dir ./cache/datalab/models/table_recognition/2025_02_18
huggingface-cli download xiaoyao9184/surya_layout --repo-type model --revision 2025_02_18 --local-dir ./cache/datalab/models/layout/2025_02_18
huggingface-cli download xiaoyao9184/surya_ocr_error_detection --repo-type model --revision 2025_02_18 --local-dir ./cache/datalab/models/ocr_error_detection/2025_02_18
```

### use surya-s3-model-download.py

```bash
python ./surya-s3-model-download.py
```
