import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { Message } from './message';

@Injectable()
export class MessagesService {
    constructor(private http: HttpClient) { }

    public getMessages(): Observable<Message[]> {
        return this.http.get<Message[]>('/api/messages')
    }

    public getMessage(messageId: number): Observable<Message> {
        return this.http.get<Message>('/api/message/' + messageId);
    }

    public sendMessage(telegramId: string, text: string): void {
        //this.http.post<Message>('/api/message/' + messageId);
        let data = new FormData();
        data.append('text', text);
        data.append('telegram_id', telegramId) 
        this.http.post("/api/send_to_user",data)
            .subscribe(
                data => {
                    console.log("POST Request is successful ", data);
                },
                error => {

                    console.log("Error", error);

                }

            );
    }
}