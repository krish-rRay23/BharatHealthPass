# BHP Healthcare - Android App

A thin mobile application for Patient and Hospital Operational modes. All business logic is handled by the backend.

## Features
- **Patient Mode**: Identity QR, profile, document upload, treatment history, consent management.
- **Hospital Mode**: Device registration, camera-based QR scanning, treatment lifecycle (start/complete).
- **Security**: Encrypted storage, JWT authentication, Firebase OTP (with Dev Mode bypass).
- **Resilience**: Room-based sync queue for offline support.

## Architecture
- **Clean Architecture**: UI -> Domain -> Data.
- **Tech Stack**: Kotlin, Jetpack Compose, Hilt, Retrofit, Room, WorkManager, Firebase.

## Setup
1. **Firebase**:
   - Create a project in Firebase Console.
   - Add an Android app with package `com.example.bhp`.
   - Download `google-services.json` and place it in the `app/` directory.
   - Enable Phone Authentication in Firebase.
2. **Backend**:
   - Update the base URL in `AppModule.kt`.
3. **Build**:
   - Run `./gradlew assembleDebug`.

## Dev Mode
Enable "Dev Mode" on the login screen to bypass Firebase OTP. Use OTP: `123456`.

## Security Rules
- No PII in QR codes.
- No Aadhaar numbers stored locally.
- Eligibility logic resides strictly on the backend.
- JWT stored in `EncryptedSharedPreferences`.
