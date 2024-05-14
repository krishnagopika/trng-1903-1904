# Lecture Plan

1. KMS
2. Cloud Trail

---

# KMS (Key Management Service)

### Encryption on flight (SSL)

- Data is encrypted before sending and decryped after receiving.
- SSL certificates help wit encryption (HTTPS).
- Encryption in flight ensures no MITM (man in the middle attack) can happen.

#### Encryption

**Server side encryption at rest**

- Data is encrypted after being recieved by the server
- Data is decrypted before being sent
- It is stored in an encrypted form using the kwy (usually a data key)
- The encryption/decryption keys must be managed somewhere and the server must have access to it.

**Client side encryption at rest**

- Data is encrypted at the client and never decrypted by the server
- Data will be decrypted by a recieveing client
- the server should not be able to decrypt te data
- could leverage envolupe encyption

## AWS KMS

- Anytime "encryption" is used for an AWS service, it's most likely KMS
- AWS manages encryption keys
- It is fully integrated with IAM for autorization
- easy access control to data
- KMS key usage can be audited using CloudTrail
- seamlessly integrated into most AWS services (EBS, S3, and RDS etc)
- KMS is also available through API calls (SDK, CLI)
- encrypted secrets can be stored in the code/environment variables

## KMS Keys Types

- previously called as KMS Customer Master Key.

1. Symmetric (AES-256 keys)
    - single encryption key that is used to Encrypt and Decrypt
    - AWS services that are integrated with KMS use Symmetric CMKs 
    - you will never get access to the KMS key unencrypted.( KMS API calls are required)
2. Asymmetric (RSA & ECC key Paris)
    - Public(Encrypt) and Private Key (Decrypt) pair
    - used to encrypt/decrypt or sign/verify operations
    - the public key is downlodable, but you can't access the private key unencrypted
    - use case: encrypton outside of AWS users who can't call the KMS API

### Types of KMS Keys

- AWS Owned Keys(free): SSE-S3, SSE-SQS, SSE-DDB(default key)
- AWS managed Key: free (aws/service-name, ex: aws/rds or aws/ebs)
- Customer managed keys created in KMS : : $1/month + pay for API call to KMS ($0.03/1000 calls)

**Automatic key roatation:**

- AWS-managed KMS Key: automatic every 1 year
- Customer-managed KMS Key: (must be enabled) every 1 year
- Imported KMS Key: only manual roatation possible using alias

**KMS Keys are region specific**

**KMS Key Policies:**

- Default: created when noting is provided, only to root user 
- Custom : only selected users can access



**KMS Symetric Key**


1. encryption

```
 aws kms encrypt --key-id 08d7d77f-dd9c-4818-8c01-af938af5ea5c --plaintext fileb://file-name.txt --output text --query CiphertextBlob --region us-east-1 > EncryptedSecretFile.base64
```

2. base64 decode

```
cat EncryptedSecretFile.base64 | base64 --decode > EncryptedSecretBinary
```

3. decrypt

```
aws kms decrypt --ciphertext-blob fileb://EncryptedSecretBinary --output text --query Plaintext > DecryptedSecret.base64 --region us-east-1
```

4. base64 decode

```
cat DecryptedSecret.base64 | base64 --decode > DecryptedSecretText
```


[AWS SDK for KMS Encryption](https://docs.aws.amazon.com/kms/latest/developerguide/programming-encryption.html)

### Envelope Encryption (GenerateDataKey API)

- over 4KB encryption
- KMS provides a plain text data encryption key is used to encrypt data on clinet side.
- KMS provides a encrypted DEK. Both encyypted DEK and the encrypted file are handeled as an envelope.
- KMS decryptes the encrypted DEK with Decrypt api call
- the decryoted DEK can be used decrypt the encrypted file.
- AWS Ecryption SDK implementes Envolupe encryption.(supports java, Python, C, JavaScript)