-- Funnel reconstruction using event-level data
SELECT
  event_name,
  COUNT(DISTINCT user_id) AS users
FROM events
WHERE event_name IN (
  'app_opened',
  'onboarding_started',
  'personal_data_completed',
  'document_screen_viewed',
  'document_submitted',
  'identity_approved'
)
GROUP BY event_name;