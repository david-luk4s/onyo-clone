import { Component, OnInit } from '@angular/core';

import { ApiService } from '../api.service';

@Component({
  selector: 'app-restaurante',
  templateUrl: './restaurante.component.html',
  styleUrls: ['./restaurante.component.css']
})
export class RestauranteComponent implements OnInit {

  restaurant = {name: '', email: '', phone: '', name_restaurant: '', address: '', message: '' };
  status = '';
  status_error = '';

  constructor(private api: ApiService) { }

  ngOnInit() {
  }


  clickedSaveRestaurant = () => {

    this.api.newRestaurant(this.restaurant).subscribe(
      data => {
        this.status = 'Registrado com sucesso :)';
        this.restaurant = {name: '', email: '', phone: '', name_restaurant: '', address: '', message: '' };
      },
      error => {
        this.status_error = 'Algo não deu certo :(';
      }
    );

  }
}
