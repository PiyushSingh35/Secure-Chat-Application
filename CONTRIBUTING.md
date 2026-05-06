# Contributing to Secure Chat Application

We welcome contributions from the community! Here's how you can help improve this project.

---

## How to Contribute

### Step 1: Fork the Repository

Click the Fork button on GitHub to create your own copy of the project.

### Step 2: Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/Secure-Chat-Application.git
cd Secure-Chat-Application
```

### Step 3: Create a Feature Branch

```bash
git checkout -b feature/YourFeature
```

Use descriptive branch names:
- feature/add-user-authentication
- bugfix/fix-encryption-issue
- docs/improve-readme

### Step 4: Make Your Changes

Edit the code and test thoroughly before committing.

### Step 5: Test Your Changes

Run the application with your changes:

```bash
python main.py
```

Verify:
- No errors or exceptions
- Functionality works as expected
- Encryption/decryption works correctly
- No performance degradation

### Step 6: Commit Your Changes

```bash
git add .
git commit -m "Add YourFeature: Brief description of what was added"
```

Use clear, descriptive commit messages.

### Step 7: Push to Your Fork

```bash
git push origin feature/YourFeature
```

### Step 8: Create a Pull Request

Go to the original repository and click "New Pull Request". Describe your changes clearly.

---

## Code Style Guide

Follow these standards for consistency:

### Python Code Style

- Use 4 spaces for indentation (NOT tabs)
- Follow PEP 8 style guide
- Use meaningful variable names
- Add comments for complex logic
- Keep functions small and focused

Example:

```python
def encrypt_message(key, plaintext):
    """
    Encrypt a plaintext message using AES-256-GCM.
    
    Args:
        key: 32-byte encryption key
        plaintext: String message to encrypt
        
    Returns:
        bytes: Encrypted data (nonce + ciphertext + auth_tag)
    """
    iv = os.urandom(12)
    cipher = crypto.createCipheriv('aes-256-gcm', key, iv)
    # ... rest of implementation
```

### Variable Naming

- Functions: lowercase_with_underscores
- Constants: UPPERCASE_WITH_UNDERSCORES
- Classes: CamelCase
- Private variables: _leading_underscore

### Comments

Good comments:
- Explain WHY not WHAT
- Describe complex algorithms
- Add docstrings to functions
- Use # for single line, """ """ for multi-line docs

Bad comments:
```python
x = x + 1  # Add 1 to x (obvious!)
```

Good comments:
```python
message_count += 1  # Track number of messages for rate limiting
```

---

## Areas for Contribution

We welcome improvements in:

Areas | Details
------|--------
Encryption | Add Diffie-Hellman key exchange, implement TLS
Networking | Support multiple clients, improve reliability
GUI | Better UI/UX with modern design
Documentation | Improve README, add tutorials
Testing | Add unit tests, integration tests
Performance | Optimize encryption speed, reduce memory usage
Security | Add authentication, implement message signing
Features | File transfer, message history, user profiles

---

## Bug Reports

Found a bug? Please report it with:

1. Clear description of the problem
2. Steps to reproduce
3. Expected behavior
4. Actual behavior
5. Python version and OS
6. Error message/traceback

Example:

Title: Encryption fails with large files

Description:
When uploading files larger than 10MB, the encryption fails with an error.

Steps to Reproduce:
1. Run the application
2. Try to encrypt a 15MB file
3. Error occurs

Expected: File should encrypt successfully
Actual: ValueError: buffer too large

System: Python 3.9 on Windows 10

---

## Feature Requests

Have an idea? Submit a feature request with:

1. Clear description of the feature
2. Why it would be useful
3. Possible implementation approach

Example:

Title: Add message encryption timestamp

Description:
Show when each message was encrypted/decrypted to verify timing.

Usefulness:
Helps debug connection issues and verify proper operation.

Implementation:
Add timestamp to encrypted payload, display in UI.

---

## Testing Guidelines

Before submitting a pull request:

1. Test locally on your machine
2. Test encryption/decryption with different key sizes
3. Test networking on same LAN
4. Test networking across different networks (with ngrok)
5. Test error handling (firewall blocks, network down, etc.)
6. Check for memory leaks (run for extended periods)
7. Verify no personal data is exposed

Test Checklist:

```
[ ] Application starts without errors
[ ] Server accepts client connections
[ ] Messages encrypt/decrypt correctly
[ ] Messages display in correct order
[ ] Connection handles interruptions gracefully
[ ] No memory leaks over extended use
[ ] Works with Python 3.8+
[ ] Firewall rules don't block traffic
```

---

## Documentation

If you add a feature:

1. Update README.md with new functionality
2. Add docstrings to new functions
3. Add code comments for complex logic
4. Update Future Improvements section if applicable
5. Add examples if applicable

---

## Commit Message Format

Use clear, descriptive commit messages:

Format:

```
Type: Short description

Longer explanation of what was changed and why.

Type can be:
- Feature: New functionality
- Bugfix: Bug fix
- Docs: Documentation changes
- Style: Code style improvements
- Refactor: Code refactoring without feature changes
- Perf: Performance improvements
```

Examples:

Good:
```
Feature: Add message timestamp tracking

Implemented timestamp encryption in payload to track when
messages were sent/received. Helps debug timing issues.
```

Bad:
```
fixed stuff
```

---

## Pull Request Guidelines

When submitting a pull request:

1. Provide clear title and description
2. Reference any related issues
3. List changes made
4. Mention testing done
5. Follow code style guidelines
6. Keep changes focused (one feature per PR)

Example PR Description:

Title: Add AES key rotation functionality

Description:
Implements automatic key rotation every N messages to improve security.

Changes:
- Added rotate_key() function in encryption.py
- Modified encrypt() to check rotation threshold
- Updated UI to show rotation status

Testing:
- Tested key rotation with 1000+ messages
- Verified decryption works after rotation
- No performance degradation observed

Related Issues: #15

---

## Code Review Process

1. Maintainers review your code
2. Feedback and suggestions provided
3. Make requested changes
4. Code approved and merged

Be open to feedback. Code reviews help maintain quality!

---

## Development Setup

To set up development environment:

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/Secure-Chat-Application.git
cd Secure-Chat-Application

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py

# Verify installation
python -c "from encryption import encrypt, decrypt; print('Success!')"
```

---

## Code of Conduct

Be respectful and professional:

- Treat everyone with respect
- Welcome newcomers
- Provide constructive feedback
- No harassment, discrimination, or hostile behavior
- Focus on ideas, not individuals

---

## Questions?

If you have questions about contributing:

1. Check existing documentation
2. Look at previous issues and PRs
3. Open a new issue asking for help
4. Email the maintainer

---

## Recognition

Contributors will be:

- Listed in README contributors section
- Acknowledged in release notes
- Credited for significant contributions

---

Thank you for contributing to Secure Chat Application!

Together we can build better security tools for everyone.
