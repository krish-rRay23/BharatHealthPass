package com.example.bhp.data.local

import androidx.room.*
import kotlinx.coroutines.flow.Flow

@Entity(tableName = "sync_queue")
data class SyncAction(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,
    val payload: String,
    val createdAt: Long = System.currentTimeMillis()
)

@Dao
interface SyncQueueDao {
    @Insert
    suspend fun insertAction(action: SyncAction)

    @Query("SELECT * FROM sync_queue ORDER BY createdAt ASC")
    fun getAllActions(): Flow<List<SyncAction>>

    @Delete
    suspend fun deleteAction(action: SyncAction)
}

@Database(entities = [SyncAction::class], version = 1)
abstract class BHPDatabase : RoomDatabase() {
    abstract fun syncQueueDao(): SyncQueueDao
}