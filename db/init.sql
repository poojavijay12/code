-- Sample initialization script
-- This will run automatically when the container starts

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email)
VALUES
('Pooja', 'pooja@example.com'),
('Admin', 'admin@example.com');
