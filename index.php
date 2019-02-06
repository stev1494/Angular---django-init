<?php include('complements/head.php') ?>
	
	</head>

	<body>
        <?php include('complements/menu.php') ?>
		<header>

		</header>
		<!--Carousel-->
		<?php include('complements/carousel.php') ?>

		<!--Contenido de la Pagina-->
		<div class="container mt-5">
			<!--Descripcion de la pagina-->
			<?php include('complements/descripcion.php') ?>
			<!--Servicios que ofrece-->
			<?php include('complements/services.php') ?>
			<!--Horarios de atención-->
			<?php include('complements/horario.php') ?>
			<!--Testimonios-->
			<?php include('complements/testimonios.php') ?>
            <div class="container d-none d-lg-block lineatiempo">
                <div class="page-header my-4">
                    <h1 id="timeline">Timeline: Redes Sociales</h1>
                </div>
                <ul class="timeline">
                    <li>
                        <div class="timeline-badge primary"><i class="fa fa-check-square" aria-hidden="true"></i></div>
                        <div class="timeline-panel">
                            <div class="timeline-heading">
                                <h4 class="timeline-title">News Title Here</h4>
                                <p><small class="text-muted"><i class="fa fa-calendar" aria-hidden="true"></i> 11 hours ago</small></p>
                            </div>
                            <div class="timeline-body">
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto illo delectus...</p>
                            </div>
                        </div>
                    </li>
                    <li class="timeline-inverted">
                        <div class="timeline-badge primary"><i class="fa fa-check-square" aria-hidden="true"></i></div>
                        <div class="timeline-panel">
                            <div class="timeline-heading">
                                <h4 class="timeline-title">News Title Here</h4>
                                <p><small class="text-muted"><i class="fa fa-calendar" aria-hidden="true"></i> 11 hours ago</small></p>
                            </div>
                            <div class="timeline-body">
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto illo delectus...</p>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="timeline-badge primary"><i class="fa fa-check-square" aria-hidden="true"></i></div>
                        <div class="timeline-panel">
                            <div class="timeline-heading">
                                <h4 class="timeline-title">News Title Here</h4>
                                <p><small class="text-muted"><i class="fa fa-calendar" aria-hidden="true"></i> 11 hours ago</small></p>
                            </div>
                            <div class="timeline-body">
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto illo delectus...</p>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
		</div>
		<!--footer-->
		<?php include('complements/footer.php') ?>
		<!--Fin Body -->
	<?php include('complements/script_slider.php') ?>
	</body>
</html>

