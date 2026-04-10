# Bharat Health Pass: Privacy by Design & DPDP Act 2023 Compliance

## 1. Zero-PII QR Protocol
The patient identity QR code does NOT contain raw Aadhaar, phone numbers, or health history.
Instead, it encodes an ephemeral, signed token containing only an opaque GUID (`sub`) and digital signature.

## 2. Dynamic Consent Revocation
In accordance with the Digital Personal Data Protection (DPDP) Act 2023, consent artefacts allow patients to:
- Review which hospital is accessing their electronic health records.
- Restrict scope to `TREATMENT_AUTH_ONLY`.
- Revoke consent at any instant via the Android client, which immediately notifies the ABDM Gateway.

## 3. Ephemeral Cache Retention
Health records fetched from the HIP are kept in transient Redis memory only during active claim adjudication.
Upon final settlement voucher generation, diagnostic files are purged from the intermediate cache.
