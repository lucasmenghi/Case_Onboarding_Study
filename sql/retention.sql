-- Upload behavior and approval conversion
SELECT
  upload_choice,
  COUNT(*) AS users,
  AVG(approved) AS approval_rate,
  AVG(document_submitted) AS document_submission_rate
FROM onboarding_users
GROUP BY upload_choice;