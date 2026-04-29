# Fixes Needed for flytoaustralia.com

## Issue 1: Itinerary builder doesn't work
- Root cause: itineraries.html does NOT link any JS file
- Fix: Add `<script src="js/itinerary-builder-fixed.js"></script>` just before `</body>` in itineraries.html

## Issue 2: Contact form is unstyled (looks 1990)
- contact.html has no JS for form submission
- The contact form needs proper styling for inputs, textareas, buttons
- CSS was added for .form-group, .contact-form-section etc but form needs JS for preview/validation

## Issue 3: Text margins jammed on multiple pages
- blog.html, contact.html, resources.html, about.html, student-visa-guide.html, etc. need proper text spacing
- The .main-content and .article-content sections need margin-bottom on paragraphs
- Check that .content-section p has margin-bottom: 1rem

## Issue 4: Several pages missing proper padding
- The CSS was added but verify all pages render with proper spacing

## Instructions
1. Fix all issues above
2. Test locally if possible (python3 -m http.server)
3. Report back ONLY the list of files changed and what was fixed
