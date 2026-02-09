package com.example.bhp.ui.screens.auth

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import kotlinx.coroutines.flow.collectLatest

@Composable
fun LoginScreen(
    onLoginSuccess: () -> Unit,
    viewModel: LoginViewModel = hiltViewModel()
) {
    val snackbarHostState = remember { SnackbarHostState() }

    LaunchedEffect(Unit) {
        viewModel.loginEvents.collectLatest { event ->
            when (event) {
                is LoginViewModel.LoginEvent.Success -> onLoginSuccess()
                is LoginViewModel.LoginEvent.Error -> snackbarHostState.showSnackbar(event.message)
            }
        }
    }

    Scaffold(
        snackbarHost = { SnackbarHost(snackbarHostState) }
    ) { padding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .padding(16.dp),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text("BHP Healthcare", style = MaterialTheme.typography.headlineLarge)
            Spacer(modifier = Modifier.height(32.dp))

            OutlinedTextField(
                value = viewModel.phoneNumber,
                onValueChange = { viewModel.phoneNumber = it },
                label = { Text("Phone Number") },
                modifier = Modifier.fillMaxWidth(),
                enabled = !viewModel.isLoading
            )

            if (viewModel.isOtpSent) {
                Spacer(modifier = Modifier.height(16.dp))
                OutlinedTextField(
                    value = viewModel.otp,
                    onValueChange = { viewModel.otp = it },
                    label = { Text("OTP") },
                    modifier = Modifier.fillMaxWidth(),
                    enabled = !viewModel.isLoading
                )
            }

            Spacer(modifier = Modifier.height(24.dp))

            Button(
                onClick = { if (viewModel.isOtpSent) viewModel.onVerifyOtp() else viewModel.onSendOtp() },
                modifier = Modifier.fillMaxWidth(),
                enabled = !viewModel.isLoading
            ) {
                if (viewModel.isLoading) {
                    CircularProgressIndicator(modifier = Modifier.size(24.dp), color = MaterialTheme.colorScheme.onPrimary)
                } else {
                    Text(if (viewModel.isOtpSent) "Verify OTP" else "Send OTP")
                }
            }

            Spacer(modifier = Modifier.height(32.dp))

            Row(verticalAlignment = Alignment.CenterVertically) {
                Text("Dev Mode (Mock OTP)")
                Switch(
                    checked = viewModel.isDevMode,
                    onCheckedChange = { viewModel.toggleDevMode(it) }
                )
            }
            if (viewModel.isDevMode) {
                Text("Use OTP: 123456", style = MaterialTheme.typography.bodySmall)
            }
        }
    }
}