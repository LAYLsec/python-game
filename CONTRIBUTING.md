# Contributing to Cosmic Dungeon Quest

Thank you for your interest in contributing! We welcome all types of contributions.

## 📋 Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## 🤝 How to Contribute

### 1. Report Bugs

**Before reporting a bug:**
- Check [existing issues](https://github.com/LAYLsec/python-game/issues)
- Verify the bug is reproducible
- Test with the latest version

**When reporting, include:**
```
- Python version (python --version)
- Operating system
- Exact steps to reproduce
- Expected vs actual behavior
- Error messages or logs
- Screenshots if applicable
```

**Example bug report:**
```markdown
**Title:** Game crashes when entering Inferno biome

**Environment:**
- Python 3.10.5
- Windows 11
- Version 1.0.0

**Steps to Reproduce:**
1. Start new game
2. Choose "Hard" difficulty
3. Enter dungeon
4. Navigate to 3rd room
5. Enemy spawns as Inferno type
6. Game crashes with traceback

**Expected:** Game should continue normally
**Actual:** Game crashes with error

**Traceback:**
[paste full error here]
```

### 2. Suggest Features

**Before suggesting:**
- Check if feature already exists
- Search [existing issues](https://github.com/LAYLsec/python-game/issues?q=is%3Aissue+label%3Aenhancement)
- Consider if it fits the project scope

**When suggesting, include:**
```
- Clear description of the feature
- Why it would be useful
- Possible implementation approach
- Examples or mockups
- Related issues or discussions
```

**Example feature request:**
```markdown
**Title:** Add health potions as consumable items

**Description:**
Currently, the only way to heal is through equipment effects. Consumable potions would:
- Add strategic depth
- Create resource management gameplay
- Improve difficulty balancing

**Implementation:**
- Add "Potion" item type
- Create healing effect system
- Add drop rates for enemies
- Update inventory UI

**Example Usage:**
Press 'p' to use equipped potion for instant healing
```

### 3. Submit Code Changes

#### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/LAYLsec/python-game.git
cd python-game

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install development dependencies (optional)
pip install -r requirements-dev.txt
```

#### Code Style Guidelines

**Follow PEP 8:**
```python
# Good: Clear, readable code
def calculate_damage(ability: Ability, player: Player) -> float:
    """Calculate total damage from an ability."""
    base_damage = player.get_attack_power() * ability.damage_mult
    if random.random() < player.critical_chance:
        base_damage *= player.critical_damage
    return base_damage

# Bad: Unclear variable names
def cd(a, p):
    bd = p.gap() * a.dm
    if random.random() < p.cc:
        bd *= p.cd
    return bd
```

**Naming Conventions:**
- Classes: `PascalCase` (e.g., `Player`, `Enemy`)
- Functions/variables: `snake_case` (e.g., `get_defense()`, `current_health`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_LEVEL`, `BASE_HEALTH`)
- Private: prefix with `_` (e.g., `_initialize_abilities()`)

**Type Hints:**
```python
# Use type hints
def add_status(self, effect: StatusEffect) -> None:
    """Add status effect to character."""
    self.status_effects.append(effect)

# Return type examples
def get_defense(self) -> float:
    return self.armor + 10

def get_enemies(self) -> List[Enemy]:
    return self.current_enemies
```

**Documentation:**
```python
class Player:
    """Main player character with progression and combat.
    
    Attributes:
        name (str): Character name
        level (int): Current character level
        health (Stat): Health stat object
    """
    
    def take_damage(self, damage: float) -> float:
        """Apply damage to the player.
        
        Args:
            damage: Amount of damage to apply
            
        Returns:
            Actual damage after defense reduction
            
        Example:
            >>> player.take_damage(50)
            42.5
        """
```

#### Making Changes

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

2. **Make your changes:**
   - Keep commits small and focused
   - One feature per branch
   - Write descriptive commit messages
   
   ```bash
   git add cosmic_dungeon_quest.py
   git commit -m "Add: Potion item system with healing mechanics"
   ```

3. **Test your changes:**
   ```bash
   python cosmic_dungeon_quest.py
   # Manual testing steps
   ```

4. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request:**
   - Go to https://github.com/LAYLsec/python-game
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template
   - Click "Create Pull Request"

#### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Code style (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Build, dependencies, etc.

**Examples:**
```
feat(combat): Add potion item system

Implement consumable health potions with:
- Drop rates from enemies
- Consumption via inventory
- Healing effect system
- Rarity-based potency

Closes #42
```

```
fix(ai): Prevent enemies from fleeing immediately

Enemies were fleeing at start of combat due to
incorrect health ratio calculation.

Fixed by checking health ratio AFTER first turn.
```

### 4. Improve Documentation

Documentation is as important as code! Help by:

- **Fixing typos or unclear explanations**
- **Adding examples and use cases**
- **Creating tutorials or guides**
- **Improving formatting**
- **Translating to other languages**

**Documentation files:**
- `README.md` - Main project overview
- `CHANGELOG.md` - Version history
- `docs/GAMEPLAY.md` - Gameplay guide
- `docs/MECHANICS.md` - Technical documentation
- `docs/MODDING.md` - Modding guide

## 📊 Pull Request Process

1. **Before submitting:**
   - [ ] Code follows PEP 8 style guide
   - [ ] Added docstrings to new functions
   - [ ] Updated CHANGELOG.md
   - [ ] Tested with Python 3.8+
   - [ ] No external dependencies added
   - [ ] Commit messages are clear

2. **PR Description Template:**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   
   ## Changes Made
   - Detailed list of changes
   - Each change as separate bullet
   
   ## Testing Done
   - How was this tested?
   - Steps to reproduce
   - Expected vs actual behavior
   
   ## Related Issues
   Closes #(issue number)
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Comments added for complex code
   - [ ] Documentation updated
   - [ ] No breaking changes
   ```

3. **Review Process:**
   - Maintainer reviews code
   - Changes may be requested
   - Once approved, PR is merged
   - Thank you for contributing!

## 🎯 Priority Issues

Looking to contribute but not sure where to start?

### Good for Beginners
- Issues labeled `good-first-issue`
- Issues labeled `documentation`
- Typo fixes and minor improvements

### High Impact
- Issues labeled `enhancement`
- Performance improvements
- Bug fixes labeled `critical`

### Help Wanted
- Issues labeled `help-wanted`
- Feature requests with community interest
- Complex refactoring tasks

## 💬 Community & Support

**Questions or need help?**
- Open a [Discussion](https://github.com/LAYLsec/python-game/discussions)
- Check [GitHub Issues](https://github.com/LAYLsec/python-game/issues)
- Email maintainers

**Want to connect with other contributors?**
- Introduce yourself in Discussions
- Share ideas and feedback
- Collaborate on features

## 📚 Additional Resources

- [GitHub's Contributing Guide](https://github.com/github/docs/blob/main/CONTRIBUTING.md)
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- [Game Development Best Practices](https://gamedev.stackexchange.com/)

## 🎉 Recognition

All contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in game credits (if desired)

## 📜 License

By contributing, you agree that your contributions will be licensed under the same [MIT License](LICENSE) as the project.

---

**Thank you for making Cosmic Dungeon Quest better!** 🚀
