# Bharat Health Pass API Reference

## Endpoints

### 1. Identity & QR Scan
`POST /api/v1/identity/scan-qr`
- **Description:** Verifies patient offline/online QR token and retrieves instant demographic metadata.
- **Headers:** `Authorization: Bearer <STAFF_JWT>`

### 2. Eligibility Adjudication
`POST /api/v1/eligibility/check`
- **Payload:** `{"user_id": "...", "ward_type": "GENERAL|ICU", "estimated_cost": 50000}`
- **Response:** `{"eligible": true, "admissible_amount": 50000, "copay": 0}`

### 3. Escrow Settlement Hold
`POST /api/v1/settlement/hold`
- **Payload:** `{"case_id": "...", "hospital_id": "...", "amount": 50000}`
- **Response:** `{"auth_token": "AUTH_...", "status": "LOCKED"}`
