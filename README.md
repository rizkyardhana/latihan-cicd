# latihan-cicd

## GitHub Actions demo

Workflow `Deploy` menjalankan simulasi deployment setiap kali tag versi (`v*.*.*`) didorong. Setelah workflow di-push ke branch utama, perintah berikut membuat tiga run rilis demo dari commit yang sama:

```bash
git tag v1.0.0
git tag v2.0.0
git tag v3.0.0
git push origin v1.0.0 v2.0.0 v3.0.0
```

Untuk rilis dengan kode berbeda, buat setiap tag pada commit rilis yang sesuai. Tag harus menunjuk ke commit yang berisi workflow ini.

Untuk simulasi rollback, buka **Actions → Deploy → Run workflow**, masukkan tag yang ingin dipulihkan (misalnya `v2.0.0`), lalu jalankan workflow. Tag tersebut harus sudah ada di GitHub.

Workflow hanya memvalidasi sintaks Python dan mencatat simulasi di Actions. Workflow ini belum mengunggah aplikasi ke hosting atau server.
