# Hamed Kazemi - Flutter Developer Portfolio

A modern, responsive Flutter Web portfolio showcasing Hamed Kazemi's skills, projects, and experience as a Flutter Developer.

## 🌟 Features

### ✨ Modern UI/UX

- **Glassmorphism Design**: Beautiful backdrop filter effects with gradient backgrounds
- **Responsive Layout**: Optimized for both desktop and mobile devices
- **Smooth Animations**: Elegant transitions and hover effects
- **Material Design 3**: Latest Material Design principles

### 🎨 Theme & Localization

- **Dark/Light Theme**: Toggle between dark and light themes
- **Bilingual Support**: Persian (فارسی) and English language support
- **Dynamic Color Schemes**: Theme-aware color palettes
- **Persian Font Support**: Vazirmatn font for proper Persian text rendering

### 📱 Responsive Design

- **Mobile-First Approach**: Optimized for mobile devices
- **Adaptive Layouts**: Different layouts for different screen sizes
- **Touch-Friendly**: Optimized touch targets and interactions
- **PWA Ready**: Progressive Web App capabilities

### 🚀 Technical Features

- **GetX State Management**: Efficient state management and dependency injection
- **CustomScrollView**: Smooth scrolling with SliverAppBar
- **Gradient Animations**: Dynamic gradient changes based on scroll position
- **URL Launcher**: Direct links to projects and contact information

## 📋 Portfolio Sections

1. **Home**: Hero section with introduction and call-to-action
2. **About Me**: Personal information and description
3. **Skills**: Technical skills and expertise
4. **Projects**: Showcase of completed projects with links
5. **Work Experience**: Professional background
6. **Education**: Academic qualifications
7. **Contact**: Contact information and social media links

## 🛠️ Technologies Used

- **Flutter**: Cross-platform UI framework
- **Dart**: Programming language
- **GetX**: State management and dependency injection
- **Google Fonts**: Typography (Vazirmatn for Persian)
- **URL Launcher**: External link handling
- **Flutter Web**: Web platform support

## 🚀 Getting Started

### Prerequisites

- Flutter SDK (3.0.0 or higher)
- Dart SDK
- Web browser for testing

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd hamed_portfolio
   ```

2. **Install dependencies**

   ```bash
   flutter pub get
   ```

3. **Run the app**

   ```bash
   # For web development
   flutter run -d chrome

   # For production build
   flutter build web
   ```

4. **Serve the production build**
   ```bash
   cd build/web
   python3 -m http.server 8000
   # Or use any other web server
   ```

## 📱 Building for Production

### Web Build

```bash
flutter build web --release
```

### PWA Build

```bash
flutter build web --release --web-renderer html
```

## 🎨 Customization

### Colors

Edit `lib/utils/app_colors.dart` to customize the color scheme:

- Light theme colors
- Dark theme colors
- Gradient combinations

### Content

Update `lib/utils/app_strings.dart` to modify:

- Personal information
- Project details
- Skills list
- Contact information

### Styling

Modify the widget files in `lib/widgets/` to customize:

- Layouts
- Animations
- Typography
- Spacing

## 🌐 Localization

The app supports Persian and English languages:

- **Persian (فارسی)**: Default language with RTL support
- **English**: Secondary language with LTR support
- **Dynamic Switching**: Toggle between languages at runtime

## 🎯 Key Features Implementation

### Glassmorphic AppBar

- `BackdropFilter` with blur effects
- Gradient background with scroll-responsive color changes
- Smooth transitions and animations

### Responsive Design

- `LayoutBuilder` for adaptive layouts
- `MediaQuery` for screen size detection
- Flexible grid systems

### Theme Management

- `GetX` controllers for state management
- Dynamic theme switching
- Persistent theme preferences

## 📁 Project Structure

```
lib/
├── controllers/          # GetX controllers
│   ├── theme_controller.dart
│   └── language_controller.dart
├── screens/             # Main screens
│   └── home_screen.dart
├── widgets/             # Reusable widgets
│   ├── glassmorphic_app_bar.dart
│   ├── about_section.dart
│   ├── skills_section.dart
│   ├── projects_section.dart
│   ├── experience_section.dart
│   ├── education_section.dart
│   ├── contact_section.dart
│   └── theme_language_switcher.dart
└── utils/               # Utility classes
    ├── app_colors.dart
    └── app_strings.dart

web/                     # Web-specific files
├── index.html
└── manifest.json
```

## 🔧 Dependencies

```yaml
dependencies:
  flutter:
    sdk: flutter
  flutter_localizations:
    sdk: flutter
  get: ^4.6.6
  google_fonts: ^6.1.0
  url_launcher: ^6.2.4
  flutter_svg: ^2.0.9
  animated_text_kit: ^4.2.2
  flutter_staggered_animations: ^1.1.1
```

## 📱 Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## 🚀 Deployment

### GitHub Pages

1. Build the web app: `flutter build web`
2. Push the `build/web` folder to your repository
3. Enable GitHub Pages in repository settings

### Netlify

1. Connect your repository to Netlify
2. Set build command: `flutter build web`
3. Set publish directory: `build/web`

### Vercel

1. Connect your repository to Vercel
2. Set build command: `flutter build web`
3. Set output directory: `build/web`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Developer

**Hamed Kazemi** - Flutter Developer

- Email: hamed75kazemii@gmail.com
- Phone: (+98) 9382867267
- Location: Tehran, Pardis, Iran
- LinkedIn: [Hamed Kazemi](https://www.linkedin.com/in/hamed--kazemi)

## 🙏 Acknowledgments

- Flutter team for the amazing framework
- GetX team for state management solution
- Google Fonts for typography support
- The Flutter community for inspiration and support

---

**Built with ❤️ using Flutter**
