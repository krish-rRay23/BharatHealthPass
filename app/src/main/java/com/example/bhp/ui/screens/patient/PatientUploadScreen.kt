package com.example.bhp.ui.screens.patient

import android.net.Uri
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CloudUpload
import androidx.compose.material.icons.filled.Description
import androidx.compose.material.icons.filled.PermIdentity
import androidx.compose.material.icons.filled.PhotoCamera
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.NavController

@Composable
fun PatientUploadScreen(
    navController: NavController,
    viewModel: PatientViewModel = hiltViewModel()
) {
    var selectedUri by remember { mutableStateOf<Uri?>(null) }
    var uploadType by remember { mutableStateOf("Govt ID") }

    val pickerLauncher = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.GetContent(),
        onResult = { uri -> selectedUri = uri }
    )

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text("Upload Documents", style = MaterialTheme.typography.headlineMedium)
        Text("Your documents are processed securely by our backend.", style = MaterialTheme.typography.bodySmall)
        
        Spacer(modifier = Modifier.height(24.dp))

        Card(modifier = Modifier.fillMaxWidth()) {
            Column(modifier = Modifier.padding(16.dp)) {
                Text("Select Document Type", style = MaterialTheme.typography.titleMedium)
                Spacer(modifier = Modifier.height(8.dp))
                
                listOf("Govt ID", "Insurance Policy", "Selfie").forEach { type ->
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        RadioButton(
                            selected = uploadType == type,
                            onClick = { uploadType = type }
                        )
                        Text(type)
                    }
                }
            }
        }

        Spacer(modifier = Modifier.height(24.dp))

        OutlinedButton(
            onClick = { pickerLauncher.launch("image/*") },
            modifier = Modifier.fillMaxWidth().height(120.dp),
            shape = MaterialTheme.shapes.medium
        ) {
            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                Icon(
                    if (selectedUri == null) Icons.Default.CloudUpload else Icons.Default.Description,
                    contentDescription = null,
                    modifier = Modifier.size(48.dp)
                )
                Text(if (selectedUri == null) "Select File / Take Photo" else "File Selected: ${selectedUri?.lastPathSegment}")
            }
        }

        Spacer(modifier = Modifier.weight(1f))

        Button(
            onClick = { /* Call repository for presigned URL and upload */ },
            modifier = Modifier.fillMaxWidth(),
            enabled = selectedUri != null && !viewModel.isLoading
        ) {
            if (viewModel.isLoading) {
                CircularProgressIndicator(modifier = Modifier.size(24.dp), color = MaterialTheme.colorScheme.onPrimary)
            } else {
                Text("Upload to Secure Backend")
            }
        }
    }
}
