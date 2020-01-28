import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { error } from 'protractor';

@Component({
  selector: 'app-contato',
  templateUrl: './contato.component.html',
  styleUrls: ['./contato.component.css']
})
export class ContatoComponent implements OnInit {

  contact = {name: '', email: '', assunto: '', message: ''};
  status = '';
  status_error = '';

  constructor(private api: ApiService) { }

  ngOnInit() {
  }

  saveContact = () => {
    this.api.newContact(this.contact).subscribe(
      data => {
        this.status = 'Mensagem enviada com sucesso, em breve responderemos :)';
        this.contact = {name: '', email: '', assunto: '', message: ''};
      },
      error => {
        this.status_error = 'Algo não deu certo :(';
      }
    );
  };
}
