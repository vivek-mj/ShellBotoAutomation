import boto3
import time

def create_snapshot(volume_id, description):
    """
    Create a snapshot of the specified EBS volume.

    Args:
        volume_id (str): The ID of the EBS volume to be backed up.
        description (str): Description for the snapshot.

    Returns:
        str: The ID of the created snapshot.
    """
    ec2 = boto3.client('ec2')
    response = ec2.create_snapshot(VolumeId=volume_id, Description=description)
    snapshot_id = response['SnapshotId']
    print(f"Snapshot {snapshot_id} created for volume {volume_id}")
    return snapshot_id

def restore_snapshot(snapshot_id, volume_id):
    """
    Restore an EBS volume from the specified snapshot.

    Args:
        snapshot_id (str): The ID of the snapshot to restore from.
        volume_id (str): The ID of the EBS volume to restore.

    Returns:
        str: The ID of the restored volume.
    """
    ec2 = boto3.client('ec2')
    response = ec2.create_volume(SnapshotId=snapshot_id, VolumeType='gp2')
    restored_volume_id = response['VolumeId']
    print(f"Volume {restored_volume_id} restored from snapshot {snapshot_id}")
    return restored_volume_id

# Example usage:
if __name__ == "__main__":
    # Specify AWS credentials and region
    aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
    aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
    region_name = 'us-west-2'  # Change to your preferred region

    # Initialize the AWS session
    boto3.setup_default_session(aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key,
                                region_name=region_name)

    # Example: Create a snapshot
    volume_id = 'YOUR_VOLUME_ID'
    description = 'Backup created on ' + time.strftime('%Y-%m-%d %H:%M:%S')
    snapshot_id = create_snapshot(volume_id, description)

    # Example: Restore a volume from snapshot
    restored_volume_id = restore_snapshot(snapshot_id, volume_id)
