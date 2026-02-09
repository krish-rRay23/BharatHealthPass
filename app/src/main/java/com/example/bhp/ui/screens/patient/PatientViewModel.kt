package com.example.bhp.ui.screens.patient

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.bhp.data.remote.ProfileResponse
import com.example.bhp.data.remote.QRTokenResponse
import com.example.bhp.data.remote.ConsentResponse
import com.example.bhp.data.remote.HistoryResponse
import com.example.bhp.data.repository.PatientRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class PatientViewModel @Inject constructor(
    private val repository: PatientRepository
) : ViewModel() {

    var profile by mutableStateOf<ProfileResponse?>(null)
    var qrToken by mutableStateOf<QRTokenResponse?>(null)
    var consents by mutableStateOf<List<ConsentResponse>>(emptyList())
    var history by mutableStateOf<List<HistoryResponse>>(emptyList())
    var isLoading by mutableStateOf(false)

    init {
        loadDashboardData()
    }

    private fun loadDashboardData() {
        viewModelScope.launch {
            isLoading = true
            repository.getProfile().onSuccess { profile = it }
            repository.getConsents().onSuccess { consents = it }
            repository.getHistory().onSuccess { history = it }
            refreshQR()
            isLoading = false
        }
    }

    fun refreshQR() {
        viewModelScope.launch {
            repository.getQRToken().onSuccess { 
                qrToken = it
                // Logic to auto-refresh before expiry (e.g., delay until expiry - 10s)
            }
        }
    }

    fun grantConsent(id: String) {
        viewModelScope.launch {
            repository.grantConsent(id).onSuccess {
                consents = consents.map { if (it.id == id) it.copy(isGranted = true) else it }
            }
        }
    }
}