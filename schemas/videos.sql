-- Table: videos
CREATE TABLE videos (
  video_id UUID PRIMARY KEY,
  uploader_id UUID REFERENCES users(user_id) NOT NULL,
  title VARCHAR(255),
  description TEXT,
  upload_time TIMESTAMP NOT NULL DEFAULT NOW(),
  length_seconds INT,
  storage_path VARCHAR(512),
  metadata_json JSONB
);
