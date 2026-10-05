# CampusHub GitHub Issue Roadmap

Each issue is intentionally scoped so contributors can work in parallel.

## Beginner (20)
### 1. Add task empty-state actions
- **Title:** Add task empty-state actions
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Show useful create-task action when there are no tasks.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 2. Improve mobile task table
- **Title:** Improve mobile task table
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Make task actions usable on narrow screens.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 3. Add accessible form labels audit
- **Title:** Add accessible form labels audit
- **Difficulty:** Beginner
- **Labels:** `accessibility`, `beginner`
- **Problem:** Ensure every interactive form control has an accessible label.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 4. Add keyboard focus styles
- **Title:** Add keyboard focus styles
- **Difficulty:** Beginner
- **Labels:** `accessibility`, `beginner`
- **Problem:** Make keyboard focus visible across the app.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 5. Add notes empty state
- **Title:** Add notes empty state
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Improve the empty notes screen with a clear call to action.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 6. Add resource subject filter UI
- **Title:** Add resource subject filter UI
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Expose subject filtering on resources.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 7. Add announcement priority filter UI
- **Title:** Add announcement priority filter UI
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Expose priority filtering on announcements.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 8. Add task due-soon filter
- **Title:** Add task due-soon filter
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Add a filter for tasks due within seven days.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 9. Add profile avatar initials
- **Title:** Add profile avatar initials
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Improve avatar fallback and accessibility.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 10. Add notification unread indicator
- **Title:** Add notification unread indicator
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Show unread count in navigation.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 11. Add API response tests
- **Title:** Add API response tests
- **Difficulty:** Beginner
- **Labels:** `testing`, `beginner`
- **Problem:** Cover response shape for core endpoints.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 12. Add validation tests
- **Title:** Add validation tests
- **Difficulty:** Beginner
- **Labels:** `testing`, `beginner`
- **Problem:** Cover invalid dates, URLs and field lengths.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 13. Document API examples
- **Title:** Document API examples
- **Difficulty:** Beginner
- **Labels:** `documentation`, `beginner`
- **Problem:** Add curl examples for common endpoints.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 14. Expand setup troubleshooting
- **Title:** Expand setup troubleshooting
- **Difficulty:** Beginner
- **Labels:** `documentation`, `beginner`
- **Problem:** Document common Windows/Linux setup failures.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 15. Add contribution issue labels guide
- **Title:** Add contribution issue labels guide
- **Difficulty:** Beginner
- **Labels:** `documentation`, `beginner`
- **Problem:** Explain label meanings and difficulty levels.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 16. Add 404 navigation link
- **Title:** Add 404 navigation link
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Give users a useful path back from errors.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 17. Add loading state to resources
- **Title:** Add loading state to resources
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Show loading feedback during API filtering.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 18. Add loading state to announcements
- **Title:** Add loading state to announcements
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Show loading feedback during API filtering.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 19. Add no-results search states
- **Title:** Add no-results search states
- **Difficulty:** Beginner
- **Labels:** `frontend`, `beginner`
- **Problem:** Differentiate no data from no search matches.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 20. Add basic template smoke tests
- **Title:** Add basic template smoke tests
- **Difficulty:** Beginner
- **Labels:** `testing`, `beginner`
- **Problem:** Verify important page routes render successfully.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.


## Intermediate (20)
### 21. Add task editing modal
- **Title:** Add task editing modal
- **Difficulty:** Intermediate
- **Labels:** `features`, `intermediate`
- **Problem:** Allow students to edit all task fields from the UI.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 22. Add note pagination
- **Title:** Add note pagination
- **Difficulty:** Intermediate
- **Labels:** `backend`, `intermediate`
- **Problem:** Paginate large note collections.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 23. Add task pagination
- **Title:** Add task pagination
- **Difficulty:** Intermediate
- **Labels:** `backend`, `intermediate`
- **Problem:** Paginate task API responses.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 24. Add resource editing
- **Title:** Add resource editing
- **Difficulty:** Intermediate
- **Labels:** `admin`, `intermediate`
- **Problem:** Allow admins to edit existing resources.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 25. Add announcement editing
- **Title:** Add announcement editing
- **Difficulty:** Intermediate
- **Labels:** `admin`, `intermediate`
- **Problem:** Allow admins to edit existing announcements.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 26. Add user management actions
- **Title:** Add user management actions
- **Difficulty:** Intermediate
- **Labels:** `admin`, `intermediate`
- **Problem:** Allow admins to deactivate accounts safely.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 27. Add announcement notifications
- **Title:** Add announcement notifications
- **Difficulty:** Intermediate
- **Labels:** `notifications`, `intermediate`
- **Problem:** Create in-app notifications for new important announcements.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 28. Add deadline calendar view
- **Title:** Add deadline calendar view
- **Difficulty:** Intermediate
- **Labels:** `features`, `intermediate`
- **Problem:** Add a simple month/calendar representation of deadlines.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 29. Add weekly productivity chart
- **Title:** Add weekly productivity chart
- **Difficulty:** Intermediate
- **Labels:** `analytics`, `intermediate`
- **Problem:** Show weekly completed-task totals using real data.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 30. Add task category counts
- **Title:** Add task category counts
- **Difficulty:** Intermediate
- **Labels:** `analytics`, `intermediate`
- **Problem:** Show category distribution on dashboard.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 31. Add sorting controls
- **Title:** Add sorting controls
- **Difficulty:** Intermediate
- **Labels:** `frontend`, `intermediate`
- **Problem:** Allow sorting tasks by due date, priority and created time.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 32. Add password change flow
- **Title:** Add password change flow
- **Difficulty:** Intermediate
- **Labels:** `auth`, `intermediate`
- **Problem:** Let authenticated users change their password.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 33. Add login rate limiting
- **Title:** Add login rate limiting
- **Difficulty:** Intermediate
- **Labels:** `security`, `intermediate`
- **Problem:** Limit repeated login attempts without locking out normal users.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 34. Add CSP security headers
- **Title:** Add CSP security headers
- **Difficulty:** Intermediate
- **Labels:** `security`, `intermediate`
- **Problem:** Add a practical content security policy.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 35. Add database indexes review
- **Title:** Add database indexes review
- **Difficulty:** Intermediate
- **Labels:** `database`, `intermediate`
- **Problem:** Review indexes for common filters and foreign keys.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 36. Add service layer for resources
- **Title:** Add service layer for resources
- **Difficulty:** Intermediate
- **Labels:** `backend`, `intermediate`
- **Problem:** Move admin resource rules into a focused service.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 37. Add API integration test suite
- **Title:** Add API integration test suite
- **Difficulty:** Intermediate
- **Labels:** `testing`, `intermediate`
- **Problem:** Test browser-to-database API workflows.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 38. Add reusable modal partial
- **Title:** Add reusable modal partial
- **Difficulty:** Intermediate
- **Labels:** `frontend`, `intermediate`
- **Problem:** Reduce repeated modal markup safely.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 39. Add pagination component
- **Title:** Add pagination component
- **Difficulty:** Intermediate
- **Labels:** `frontend`, `intermediate`
- **Problem:** Create a reusable pagination template/component.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 40. Add contributor setup script
- **Title:** Add contributor setup script
- **Difficulty:** Intermediate
- **Labels:** `devops`, `intermediate`
- **Problem:** Provide a one-command local setup helper.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.


## Advanced (10)
### 41. Add audit log
- **Title:** Add audit log
- **Difficulty:** Advanced
- **Labels:** `security`, `advanced`
- **Problem:** Record important admin actions without exposing sensitive data.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 42. Add optimistic task updates
- **Title:** Add optimistic task updates
- **Difficulty:** Advanced
- **Labels:** `frontend`, `advanced`
- **Problem:** Update task status immediately and reconcile server failures.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 43. Add database migration workflow
- **Title:** Add database migration workflow
- **Difficulty:** Advanced
- **Labels:** `database`, `advanced`
- **Problem:** Introduce repeatable migrations without breaking existing databases.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 44. Add API versioning
- **Title:** Add API versioning
- **Difficulty:** Advanced
- **Labels:** `backend`, `advanced`
- **Problem:** Version public API endpoints for contributor stability.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 45. Add role/permission service
- **Title:** Add role/permission service
- **Difficulty:** Advanced
- **Labels:** `security`, `advanced`
- **Problem:** Centralize authorization rules for future roles.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 46. Add query performance dashboard
- **Title:** Add query performance dashboard
- **Difficulty:** Advanced
- **Labels:** `database`, `advanced`
- **Problem:** Measure slow queries in a local development mode.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 47. Add notification deduplication service
- **Title:** Add notification deduplication service
- **Difficulty:** Advanced
- **Labels:** `notifications`, `advanced`
- **Problem:** Prevent repeated generated reminders across requests.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 48. Add test coverage gate
- **Title:** Add test coverage gate
- **Difficulty:** Advanced
- **Labels:** `devops`, `advanced`
- **Problem:** Fail CI when coverage falls below an agreed threshold.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 49. Add security dependency scanning
- **Title:** Add security dependency scanning
- **Difficulty:** Advanced
- **Labels:** `devops`, `advanced`
- **Problem:** Add dependency vulnerability checks to CI.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.

### 50. Add production deployment guide
- **Title:** Add production deployment guide
- **Difficulty:** Advanced
- **Labels:** `devops`, `advanced`
- **Problem:** Document safe deployment with HTTPS, secrets and persistent database storage.
- **Expected behavior:** The change works through the existing Flask/Jinja/vanilla-JS architecture and persists or validates data where applicable.
- **Acceptance criteria:** Feature is implemented; invalid input is handled; affected routes/UI work; tests are added or updated; existing tests still pass.
- **Files likely affected:** Relevant module under `app/routes`, `app/services`, `app/templates`, `app/static`, `app/models`, plus `tests/` and docs when needed.
- **Testing required:** `pytest -q` plus manual verification of the affected page/API.
