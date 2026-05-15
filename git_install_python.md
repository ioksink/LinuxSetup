Due to the change of qobuz login method, authentication method should be changed to uid, token.

As in [guyathomas's fork](https://github.com/guyathomas/qobuz-dl/tree/feat/token-auth-poc) from [master branch](https://github.com/vitiko98/qobuz-dl/tree/master).

The fork is pulled with `git -b feat/token-auth-poc --single-branch https://github.com/vitiko98/qobuz-dl.git` and then installed with

```zsh
cd qobuz-dl
sudo pip install -e .
```

For uninstall, `sudo pip uninstall qobuz-dl`