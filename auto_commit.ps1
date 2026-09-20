while($true) { $status = git status --porcelain; if ($status) { git add .; git commit -m "Auto-commit"; git push }; Start-Sleep -Seconds 300 }
