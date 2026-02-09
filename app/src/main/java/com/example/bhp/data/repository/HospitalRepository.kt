package com.example.bhp.data.repository

import com.example.bhp.data.remote.*
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class HospitalRepository @Inject constructor(
    private val api: BHPService
) {
    suspend fun registerDevice(): Result<DeviceRegistrationResponse> {
        return try {
            val response = api.registerDevice()
            if (response.isSuccessful && response.body() != null) {
                Result.success(response.body()!!)
            } else {
                Result.failure(Exception("Registration failed"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun submitScan(token: String): Result<ScanResultResponse> {
        return try {
            val response = api.submitScan(mapOf("token" to token))
            if (response.isSuccessful && response.body() != null) {
                Result.success(response.body()!!)
            } else {
                Result.failure(Exception("Scan submission failed"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun startTreatment(authId: String): Result<Unit> {
        return try {
            val response = api.startTreatment(authId)
            if (response.isSuccessful) Result.success(Unit) else Result.failure(Exception("Failed to start"))
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun completeTreatment(authId: String): Result<Unit> {
        return try {
            val response = api.completeTreatment(authId)
            if (response.isSuccessful) Result.success(Unit) else Result.failure(Exception("Failed to complete"))
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}