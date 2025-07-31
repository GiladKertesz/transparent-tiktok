-- Table: interactions
CREATE TABLE interactions (
  interaction_id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(user_id) NOT NULL,
  video_id UUID REFERENCES videos(video_id) NOT NULL,
  type VARCHAR(20) NOT NULL CHECK (type IN ('view','like','share','comment')),
  timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
  duration_watched INT
);
