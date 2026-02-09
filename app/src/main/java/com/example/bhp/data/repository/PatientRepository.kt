package com.example.bhp.data.repository

import com.example.bhp.data.remote.BHPService
import com.example.bhp.data.remote.ProfileResponse
import com.example.bhp.data.remote.QRTokenResponse
import com.example.bhp.data.remote.ConsentResponse
import com.example.bhp.data.remote.HistoryResponse
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class PatientRepository @Inject constructor(
    private val api: BHPService
) {
    suspend fun getProfile(): Result<ProfileResponse> {
        return try {
            val response = api.getProfile()
            if (response.isSuccessful && response.body() != null) {
                Result.success(response.body()!!)
            } else {
                Result.failure(Exception("Failed to fetch profile"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getQRToken(): Result<QRTokenResponse> {
        return try {
            val response = api.getQRToken()
            if (response.isSuccessful && response.body() != null) {
                Result.success(response.body()!!)
            } else {
                Result.failure(Exception("Failed to fetch QR token"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getConsents(): Result<List<ConsentResponse>> {
        return try {
            val response = api.getConsents()
            if (response.isSuccessful && response.body() != null) {
                Result.success(response.body()!!)
            } else {
                Result.failure(Exception("Failed to fetch consents"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun grantConsent(id: String): Result<Unit> {
        return try {
            val response = api.grantConsent(id)
            if (response.isSuccessful) {
                Result.success(Unit)
            } else {
                Result.failure(Exception("Failed to grant consent"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getHistory(): Result<List<HistoryResponse>> {
        return try {
            val response = api.getHistory()
            if (response.isSuccessful && response.body() != null) {
                Result.success(response.body()!!)
            } else {
                Result.failure(Exception("Failed to fetch history"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}