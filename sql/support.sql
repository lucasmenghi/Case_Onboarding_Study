-- Support demand by upload choice
SELECT
  u.upload_choice,
  COUNT(DISTINCT u.user_id) AS users,
  COUNT(DISTINCT s.call_id) AS support_calls,
  COUNT(DISTINCT s.call_id) * 1.0 / COUNT(DISTINCT u.user_id) AS support_rate
FROM onboarding_users u
LEFT JOIN support_calls s
  ON u.user_id = s.user_id
GROUP BY u.upload_choice;