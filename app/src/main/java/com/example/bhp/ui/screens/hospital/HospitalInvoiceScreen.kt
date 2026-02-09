package com.example.bhp.ui.screens.hospital

import android.net.Uri
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Receipt
import androidx.compose.material.icons.filled.UploadFile
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.NavController

@Composable
fun HospitalInvoiceScreen(
    authId: String,
    navController: NavController,
    viewModel: HospitalViewModel = hiltViewModel()
) {
    var selectedUri by remember { mutableStateOf<Uri?>(null) }

    val pickerLauncher = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.GetContent(),
        onResult = { uri -> selectedUri = uri }
    )

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text("Upload Treatment Invoice", style = MaterialTheme.typography.headlineMedium)
        Text("Auth ID: $authId", style = MaterialTheme.typography.bodySmall)
        
        Spacer(modifier = Modifier.height(24.dp))

        OutlinedButton(
            onClick = { pickerLauncher.launch("image/*") },
            modifier = Modifier.fillMaxWidth().height(150.dp),
            shape = MaterialTheme.shapes.medium
        ) {
            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                Icon(
                    if (selectedUri == null) Icons.Default.Receipt else Icons.Default.UploadFile,
                    contentDescription = null,
                    modifier = Modifier.size(64.dp)
                )
                Spacer(modifier = Modifier.height(8.dp))
                Text(if (selectedUri == null) "Select Invoice Photo" else "Invoice Selected")
            }
        }

        if (selectedUri != null) {
            Text("Ready to sync with backend OCR service.", modifier = Modifier.padding(top = 16.dp), style = MaterialTheme.typography.bodySmall)
        }

        Spacer(modifier = Modifier.weight(1f))

        Button(
            onClick = { 
                // Logic to upload invoice for specific authId
                navController.popBackStack()
            },
            modifier = Modifier.fillMaxWidth(),
            enabled = selectedUri != null && !viewModel.isLoading
        ) {
            Text("Submit for Processing")
        }
    }
}
