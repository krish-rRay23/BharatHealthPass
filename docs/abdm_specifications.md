# ABDM Integration & Milestone Architecture

## Overview
Bharat Health Pass is architected to be fully compliant with the Ayushman Bharat Digital Mission (ABDM) sandbox standards:

1. **Milestone 1 (M1): ABHA Creation & Verification**
   - Creation of 14-digit ABHA Number using Aadhaar/Phone OTP.
   - Verification of demographic details.
   - ABHA address generation (`user@abdm`).

2. **Milestone 2 (M2): Health Information Provider (HIP)**
   - Linking health records with user's ABHA.
   - Responding to ABDM discovery requests with cryptographic hash validation.
   - Transferring FHIR R4 clinical data bundles encrypted via Diffie-Hellman key exchange.

3. **Milestone 3 (M3): Health Information User (HIU)**
   - Requesting patient consent through ABDM Consent Manager (CM).
   - Receiving and validating structured Consent Artefacts.
   - Decrypting health data to perform real-time insurance underwriting and pre-authorization.
