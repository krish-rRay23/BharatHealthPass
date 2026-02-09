package com.example.bhp.data.repository

import com.example.bhp.data.local.SecurityManager
import com.example.bhp.data.remote.BHPService
import com.example.bhp.data.remote.TokenResponse
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class AuthRepository @Inject constructor(
    private val api: BHPService,
    private val securityManager: SecurityManager
) {
    suspend fun verifyToken(firebaseToken: String): Result<TokenResponse> {
        return try {
            val response = api.verifyFirebaseToken(mapOf("token" to firebaseToken))
            if (response.isSuccessful && response.body() != null) {
                val tokenBody = response.body()!!
                securityManager.saveJwt(tokenBody.token)
                Result.success(tokenBody)
            } else {
                Result.failure(Exception("Verification failed"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    fun isDevMode() = securityManager.isDevMode()
    fun setDevMode(enabled: Boolean) = securityManager.setDevMode(enabled)
    fun getJwt() = securityManager.getJwt()
    fun logout() = securityManager.clear()
}