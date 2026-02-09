package com.example.bhp.ui.screens.hospital

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.bhp.data.remote.ScanResultResponse
import com.example.bhp.data.repository.HospitalRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class HospitalViewModel @Inject constructor(
    private val repository: HospitalRepository
) : ViewModel() {

    var isDeviceApproved by mutableStateOf(false)
    var scanResult by mutableStateOf<ScanResultResponse?>(null)
    var isLoading by mutableStateOf(false)

    private val _events = MutableSharedFlow<HospitalEvent>()
    val events = _events.asSharedFlow()

    fun registerDevice() {
        viewModelScope.launch {
            isLoading = true
            repository.registerDevice().onSuccess {
                isDeviceApproved = it.status == "approved"
            }.onFailure {
                _events.emit(HospitalEvent.Error("Registration failed"))
            }
            isLoading = false
        }
    }

    fun onQrScanned(token: String) {
        viewModelScope.launch {
            isLoading = true
            repository.submitScan(token).onSuccess {
                scanResult = it
                _events.emit(HospitalEvent.ScanSuccess(it.auth_id))
            }.onFailure {
                _events.emit(HospitalEvent.Error("Scan failed: ${it.message}"))
            }
            isLoading = false
        }
    }

    fun startTreatment(authId: String) {
        viewModelScope.launch {
            repository.startTreatment(authId).onSuccess {
                _events.emit(HospitalEvent.Message("Treatment started"))
            }
        }
    }

    sealed class HospitalEvent {
        data class ScanSuccess(val authId: String) : HospitalEvent()
        data class Error(val message: String) : HospitalEvent()
        data class Message(val message: String) : HospitalEvent()
    }
}