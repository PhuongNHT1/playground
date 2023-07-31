<?php require "partials/head.php" ?>
<?php require "partials/nav.php" ?>
<?php require "partials/banner.php" ?>

<main>
  <div class="mx-auto max-w-7xl py-6 sm:px-6 lg:px-8">
    Hello to my homepage
    <ul>
      <?php foreach ($shortcuts as $shortcut) : ?>
          <li>
            <a href="/shortcut?id=<?= $shortcut['id'] ?>" class="text-blue-500 hover:underline">
              <?= $shortcut['combo'] ?>
            </a>
          </li>
      <?php endforeach ; ?>
    </ul>
    <p>
      <a href="/shortcut/create" class="text-blue-500 hover:underline">Create shortcut</a>
    </p>
  </div>
</main>


<?php require "partials/footer.php" ?>


