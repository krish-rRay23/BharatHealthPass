package com.example.bhp.data.remote

import okhttp3.MultipartBody
import retrofit2.Response
import retrofit2.http.*

interface BHPService {
    @POST("auth/firebase-verify")
    suspend fun verifyFirebaseToken(@Body body: Map<String, String>): Response<TokenResponse>

    @GET("profile")
    suspend fun getProfile(): Response<ProfileResponse>

    @POST("upload")
    suspend fun getPresignedUrl(@Body body: Map<String, String>): Response<PresignedUrlResponse>

    @POST("cards")
    suspend fun getQRToken(): Response<QRTokenResponse>

    @GET("consents")
    suspend fun getConsents(): Response<List<ConsentResponse>>

    @POST("consents/{id}/grant")
    suspend fun grantConsent(@Path("id") id: String): Response<Unit>

    @GET("history")
    suspend fun getHistory(): Response<List<HistoryResponse>>

    @POST("devices/register")
    suspend fun registerDevice(): Response<DeviceRegistrationResponse>

    @POST("scan")
    suspend fun submitScan(@Body body: Map<String, String>): Response<ScanResultResponse>

    @POST("treatment/{auth_id}/start")
    suspend fun startTreatment(@Path("auth_id") authId: String): Response<Unit>

    @POST("treatment/{auth_id}/complete")
    suspend fun completeTreatment(@Path("auth_id") authId: String): Response<Unit>
}

data class TokenResponse(val token: String, val refreshToken: String)
data class ProfileResponse(val name: String, val address: String, val emergencyContact: String, val identityConfidence: Float, val eligibilityLevel: String, val fallbackReasons: List<String>?)
data class PresignedUrlResponse(val url: String, val key: String)
data class QRTokenResponse(val token: String, val expiresAt: Long)
data class ConsentResponse(val id: String, val title: String, val description: String, val isGranted: Boolean)
data class HistoryResponse(val id: String, val treatment: String, val status: String, val date: String)
data class DeviceRegistrationResponse(val status: String)
data class ScanResultResponse(val auth_id: String, val approved_amount: Double, val identity_summary: String, val confidence: Float, val source: String)
