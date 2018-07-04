package com.thezouth.kafka201.member;

import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;


@Service
public class MemberService {
    private Map<String, Member> memberRepo;

    public MemberService(List<Member> members) {
        this.memberRepo = members.stream()
                .collect(Collectors.toMap(Member::getId, n -> n));
    }

    public Optional<Member> getMember(String memberId) {
        if (!this.memberRepo.containsKey(memberId))
            return Optional.empty();

        return Optional.of(this.memberRepo.get(memberId));
    }

    public void promoteMember(String memberId, String privilege) {
        final Member member = getMember(memberId).get();
        member.setPrivilege(privilege);
    }

    public MemberService() {
        this(List.of(
                new Member("admin-id", "admin-name", "admin-prev",
                        "admin@webscal3r.club", null, NotificationChannel.EMAIL),
                new Member("1", "YiM", "silver",
                        null, "yimyim", NotificationChannel.LINE),
                new Member("2", "Roong", "silver",
                        "abc@xyz.com", "roongroong", NotificationChannel.ALL)
        ));
    }
}
