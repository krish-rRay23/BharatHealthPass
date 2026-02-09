package com.example.bhp.data.remote

import com.example.bhp.data.local.SecurityManager
import okhttp3.Authenticator
import okhttp3.Request
import okhttp3.Response
import okhttp3.Route
import javax.inject.Inject
import javax.inject.Provider

class TokenAuthenticator @Inject constructor(
    private val securityManager: SecurityManager,
    private val apiProvider: Provider<BHPService>
) : Authenticator {
    override fun authenticate(route: Route?, response: Response): Request? {
        synchronized(this) {
            val currentToken = securityManager.getJwt()
            
            // If the request already failed with the current token, try refreshing
            if (response.request.header("Authorization") != "Bearer $currentToken") {
                return null // Already tried refreshing
            }

            // In a real app, you'd call a refresh endpoint here
            // val newTokenResponse = apiProvider.get().refreshToken(...) 
            // securityManager.saveJwt(newTokenResponse.token)
            
            // Mocking a successful refresh for demonstration
            val mockNewToken = "refreshed_jwt_token"
            securityManager.saveJwt(mockNewToken)

            return response.request.newBuilder()
                .header("Authorization", "Bearer $mockNewToken")
                .build()
        }
    }
}