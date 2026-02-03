# UX Layout Specifications - General Reference

## Overview
Reusable UX layout patterns, responsive behavior, visual feedback states, accessibility standards, and color system specifications. These patterns apply broadly across projects and complement the design tokens in `UX_DESIGN_SYSTEM.js`.

---

## 1. Responsive Behavior

### Desktop (> 1024px)
- **Layout**: Side-by-side panels (e.g., 60/40 or 50/50 split)
- **Navigation**: Full navigation visible
- **Sidebar**: Full width (200-300px typical)
- **Buttons**: Horizontal layout, no wrapping
- **Fixed elements**: Header and footer always visible

### Tablet (768px - 1024px)
- **Layout**: Stacked vertically (primary content on top, controls below)
- **Primary content**: 100% width, 50vh height
- **Controls**: 100% width, 50vh height
- **Sidebar**: Full width
- **Buttons**: May wrap to multiple rows

### Mobile (≤ 768px)
- **Layout**: Stacked vertically
- **Navigation**: Hamburger menu visible, full nav hidden
- **Primary content**: 100% width, 40vh height
- **Controls**: 100% width, 60vh height
- **Sidebar**: 100% width (remove fixed-width constraints)
- **Buttons**: Wrap to multiple rows
- **Touch Targets**: Minimum 44x44px

### Small Mobile (≤ 480px)
- **Primary content**: 35vh height
- **Controls**: 65vh height
- **Padding**: Reduced to 4px
- **Gaps**: Reduced to 8px

---

## 2. Visual Feedback & Animations

### Loading States
- **Processing**: Shimmer effect on content area, pulse animation, status text overlay
- **Saving**: Button shows loading spinner
- **Loading Data**: Skeleton loaders or spinners

### Success States
- **Action confirmation**: Button text changes temporarily (e.g., "Copied!") with color shift to green
- **Save success**: Toast notification
- **Selection confirmation**: Checkmark animation on selection

### Hover States
- **Buttons**: Lift up 2px (`translateY(-2px)`), enhanced shadow
- **List items**: Background color change to subtle tint
- **Interactive cards**: Scale up slightly (`scale(1.02)`), glow effect

### Active/Selected States
- **Active list item**: Colored left border (3px), tinted background
- **Selected option**: Checkmark icon, colored border, pulse glow animation
- **Locked/pinned item**: Distinct icon color (e.g., yellow lock icon)

### Disabled States
- **Excluded items**: Reduced opacity (0.4-0.5), grayscale filter
- **Disabled buttons**: Reduced opacity, `not-allowed` cursor, no hover effect

### Transition Defaults
- **Duration**: 0.3s ease for standard interactions
- **Ripple effect**: 300ms expanding circle from click point
- **Pulse glow**: 2s infinite for selected/active emphasis

---

## 3. Keyboard Navigation

### Tab Order
- **Sequence**: Header → Sidebar/navigation → Primary content controls → Action buttons → Footer
- **Focus rings**: Visible focus indicators (accent color, 3px outline)
- **Skip links**: Recommended for content-heavy layouts

### General Principles
- All interactive elements must be reachable via Tab key
- Focus order should follow visual reading order
- Modal dialogs should trap focus within the modal
- Focus should return to the trigger element after modal close

---

## 4. Accessibility Features

### ARIA Labels
- All interactive buttons must have `aria-label` attributes
- Tooltips provide additional context for icon-only buttons
- Landmark roles for major page sections

### Color Contrast
- Text meets WCAG AA standards (4.5:1 minimum for normal text, 3:1 for large text)
- Interactive element colors are distinguishable from surrounding content
- Disabled states are clearly indicated through multiple visual cues (not color alone)

### Touch Targets
- All buttons minimum 44x44px (WCAG 2.5.5 / mobile accessibility standard)
- Adequate spacing between interactive elements (minimum 8px gap)

### Focus Management
- Focus rings visible on keyboard navigation
- Modal dialogs trap focus within the dialog
- Focus returns to trigger element after modal/dialog close
- No focus traps outside of modal contexts

---

## 5. Color System

### Status Colors
- **Locked/Pinned**: Yellow (`#fbbf24`)
- **Success**: Green (`#10b981`, `#22c55e`)
- **Warning**: Amber (`#f59e0b`, `#fbbf24`)
- **Error/Destructive**: Red (`#ef4444`)
- **Info/Accent**: Purple (`#8b5cf6`)

### Neutral Colors
- **Text Primary**: `#2c2c2c`
- **Text Secondary**: `#6b6b6b`
- **Text Tertiary**: `#9ca3af`
- **Background Primary**: `#fefefe`
- **Background Secondary**: `#f8f6f2`
- **Borders**: `rgba(0,0,0,0.08)`

### Color Usage Patterns
- Use opacity variations (10%, 15%, 20%, 25%, 30%, 40%) for category/accent color backgrounds
- Gradients for primary action buttons (e.g., `linear-gradient` between two related hues)
- Shadows should use the accent color at low opacity (e.g., `rgba(accentColor, 0.3)`) for colored glow effects
- Destructive actions use red text/background tint to signal caution

### Common Component Styling
- **Borders**: 1px solid `rgba(0,0,0,0.08)` for subtle separation
- **Border Radius**: 8-16px for containers, 24px (pill) for action buttons, 4-8px for small elements
- **Shadows**: `0 2px 8px rgba(0,0,0,0.05)` for subtle elevation, `0 4px 12px rgba(0,0,0,0.15)` for modals/dropdowns
- **Background gradients**: Linear gradient between two near-white values for panels (e.g., `#fefefe` to `#f8f6f2`)

---

## 6. Layout Patterns

### Split-Screen (Desktop)
- Primary content area (50-60%) + controls panel (40-50%)
- Preview/content area uses sticky positioning when paired with scrollable controls
- Controls panel divided into scrollable section (top) + fixed action area (bottom)

### Fixed Header/Footer
- **Header**: Fixed top, 48-56px height, z-index 100
- **Footer**: Fixed bottom, 56-64px height, z-index 100
- **Content area**: `calc(100vh - header - footer)` for full-height layouts

### Scrollable Panels
- Vertical scroll only (`overflow-y: auto`, `overflow-x: hidden`)
- Thin scrollbar styling with accent color at 40% opacity
- Smooth scroll behavior with snap points for button/card lists

### Modal/Overlay Patterns
- **Backdrop**: `rgba(0,0,0,0.5)` overlay covering entire viewport
- **Modal panel**: White background, 8-12px border radius, elevated shadow
- **Slide-in panel**: 80% width (max 300px) from left/right edge
- **Dropdown menu**: Absolute positioned, min-width 180px, z-index 1000
- **Close behavior**: Click outside to close, Escape key to close

---

This document provides reusable layout specifications. For design tokens (spacing, typography, touch targets, animation constants), see `UX_DESIGN_SYSTEM.js`.
