package com.example.bhp.data.sync

import android.content.Context
import androidx.work.CoroutineWorker
import androidx.work.WorkerParameters
import com.example.bhp.data.local.SyncQueueDao
import com.example.bhp.data.remote.BHPService
import kotlinx.coroutines.flow.first
import javax.inject.Inject

class SyncWorker(
    context: Context,
    workerParams: WorkerParameters,
    private val dao: SyncQueueDao,
    private val api: BHPService
) : CoroutineWorker(context, workerParams) {

    override suspend fun doWork(): Result {
        val actions = dao.getAllActions().first()
        if (actions.isEmpty()) return Result.success()

        for (action in actions) {
            try {
                // Simplified sync logic
                when (action.type) {
                    "SCAN" -> api.submitScan(mapOf("token" to action.payload))
                    // Add other types...
                }
                dao.deleteAction(action)
            } catch (e: Exception) {
                // If transient, return retry
                return Result.retry()
            }
        }
        return Result.success()
    }
}