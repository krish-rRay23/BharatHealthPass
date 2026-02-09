package com.example.bhp.ui.screens.auth

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.bhp.data.repository.AuthRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class LoginViewModel @Inject constructor(
    private val repository: AuthRepository
) : ViewModel() {

    var phoneNumber by mutableStateOf("")
    var otp by mutableStateOf("")
    var isOtpSent by mutableStateOf(false)
    var isLoading by mutableStateOf(false)
    var isDevMode by mutableStateOf(repository.isDevMode())

    private val _loginEvents = MutableSharedFlow<LoginEvent>()
    val loginEvents = _loginEvents.asSharedFlow()

    fun onSendOtp() {
        viewModelScope.launch {
            isLoading = true
            // Mock OTP sending
            isOtpSent = true
            isLoading = false
        }
    }

    fun onVerifyOtp() {
        viewModelScope.launch {
            isLoading = true
            if (isDevMode && otp == "123456") {
                repository.verifyToken("mock_firebase_token")
                    .onSuccess { _loginEvents.emit(LoginEvent.Success) }
                    .onFailure { _loginEvents.emit(LoginEvent.Error(it.message ?: "Login failed")) }
            } else {
                // Real Firebase logic would go here
                _loginEvents.emit(LoginEvent.Error("Invalid OTP (use 123456 in dev mode)"))
            }
            isLoading = false
        }
    }

    fun toggleDevMode(enabled: Boolean) {
        isDevMode = enabled
        repository.setDevMode(enabled)
    }

    sealed class LoginEvent {
        object Success : LoginEvent()
        data class Error(val message: String) : LoginEvent()
    }
}