DROP TABLE IF EXISTS apps;

CREATE TABLE IF NOT EXISTS apps (
  id serial PRIMARY KEY,
  app VARCHAR(255),
  category VARCHAR(255),
  rating DECIMAL,
  reviews VARCHAR(255),
  app_size VARCHAR(255),
  installs VARCHAR(255),
  app_type VARCHAR(255),
  price VARCHAR(255),
  content_rating VARCHAR(255),
  genre VARCHAR(255),
  last_updated TIMESTAMP,
  current_ver VARCHAR(255),
  android_ver VARCHAR(255)
);